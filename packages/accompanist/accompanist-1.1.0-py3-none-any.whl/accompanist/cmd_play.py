import click
import subprocess
import random

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages as pp

import accompanist.report.write_front_cover as wf
import accompanist.report.draw_histgram as dh
import accompanist.report.draw_pie_chart as dp
import accompanist.report.draw_table as dt
import accompanist.report.write_comment as wc
import accompanist.report.utility_module as um

INPUT_CSV_FILE = "./waf-log.csv"
OUTPUT_PDF_FILE = "./report.pdf"
A4_SIZE = (11.69, 8.27)
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.command(name="play", context_settings=CONTEXT_SETTINGS,
               help="Analysis WAF logs and generate a report.")
@click.option("-c", "--colorful", required=False, is_flag=True,
              help="Set a random color of report theme (instead of color).")
@click.option("-d", "--color", required=False, type=str,
              help="Customize a color of report theme with color code,  (e.g.) #cccccc.")
@click.option("-m", "--mask-ip", required=False, is_flag=True,
              help="Mask IP addresses on pie chart.")
@click.option("-u", "--utc-offset", required=False, type=int, default=9,
              help="Set a number of UTC offest. The defaut offset is UTC+9 (Asia/Tokyo).")
@click.option("-y", "--y-limit", required=False, default="50",
              type=click.Choice(["50", "100", "500", "1000"]),
              help="Adjust a Y-axis max limitation for histograms due to many requests.")
def play(color, colorful, mask_ip, utc_offset, y_limit):

    # Pre-Process
    waf_log = pd.read_csv(INPUT_CSV_FILE, header=None)
    waf_log.columns = ["time", "rule", "uri", "ip", "country"]

    plt.rcParams["font.family"] = "Arial"

    fig_1 = plt.figure(figsize=A4_SIZE)
    fig_2 = plt.figure(figsize=A4_SIZE)
    fig_3 = plt.figure(figsize=A4_SIZE)
    fig_4 = plt.figure(figsize=A4_SIZE)
    fig_5 = plt.figure(figsize=A4_SIZE)
    fig_6 = plt.figure(figsize=A4_SIZE)

    figs = [fig_1, fig_2, fig_3, fig_4, fig_5, fig_6]

    color_list = ["#154f74", "#1397ab", "#9a540f",
                  "#ffa50d", "#74bd97", "#2fcdfa", "#f595ff", "#9a5bc0", "#000000"]

    if color is None:
        if colorful:
            index = random.randint(0, len(color_list) - 1)
            color = color_list[index]
            print("[Info] A theme color of the report was chosen randomly:", color)
        else:
            color = "#154f74"  # Default color

    # Add front cover
    wf.write_front_cover(fig_1, color)

    # Calculation & Draw
    dh.draw_histgram(waf_log, fig_2, utc_offset, y_limit)
    dp.draw_pie_chart(waf_log, fig_3, fig_4, mask_ip)
    dt.draw_table(waf_log, fig_5)
    wc.write_comment(fig_6)

    # Post-Process
    um.write_header_and_footer(waf_log["time"], figs[1:], utc_offset, color)

    pdf = pp(OUTPUT_PDF_FILE)

    for i in figs:
        pdf.savefig(i)

    pdf.close()

    subprocess.Popen("open " + OUTPUT_PDF_FILE, shell=True)
