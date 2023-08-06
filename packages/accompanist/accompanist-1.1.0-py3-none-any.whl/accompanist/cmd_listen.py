import sys
import time
import json
import csv
import datetime

import click
import boto3

SHEET_MUSIC_FILE = "sheet_music.json"
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.command(name="listen", context_settings=CONTEXT_SETTINGS,
               help="Get a WAF log file in CSV format.")
@click.option("-a", "--action", required=True, default="BLOCK",
              prompt="Please input the action of AWS WAF",
              type=click.Choice(["BLOCK", "COUNT"]),
              help="Chose an action type of AWS WAF. The default is \"BLOCK\".")
@click.option("-d", "--days", required=False, type=int, default="1",
              prompt="Please input the number of analysis target days",
              help="Set a number of the past days until today for analysis target period.")
@click.option("-s", "--start_time", required=False, type=int,
              help="Set a UNIX time of the oldest time for analysis target period (instead of \"--days\").")
@click.option("-e", "--end_time", required=False, type=int,
              help="Set a UNIX time of the latest time for analysis target period (instead of \"--days\").")
@click.option("-r", "--raw-log", required=False, is_flag=True,
              help="Output raw log file and the excerpted log file for debug.")
def listen(days, start_time, end_time, action, raw_log):

    with open("config.json", mode="r") as f:
        config_dict = json.load(f)

    log_group = config_dict["log_group"]
    client = boto3.client("logs")

    if action == "BLOCK":
        query = 'fields @timestamp, @message | filter @message like "BLOCK" | sort @timestamp desc'
    elif action == "COUNT":
        query = 'fields @timestamp, @message | filter @message like /"action":"COUNT"/ | sort @timestamp desc'
    else:
        print("Error: action is empty or invalid")
        sys.exit()

    if days is not None and (start_time is None or end_time is None):
        end_time = int(time.time())
        start_time = end_time - days * 24 * 3600
    else:
        days_warning = "[Warning] The inputted number of days is ignored as the start & end times had been set."
        print("\033[33m" + days_warning + "\033[0m")

    start_query_response = client.start_query(
        logGroupName=log_group,
        startTime=start_time,
        endTime=end_time,
        queryString=query,
        limit=10000
    )

    response = None
    print("[Info] The CloudWatch Logs Insights query started.")

    while response is None or response["status"] == "Running":
        time.sleep(3)
        print(" ... ... ... ")
        response = client.get_query_results(queryId=start_query_response["queryId"])
    print("[Info] The query has been completed!")

    if raw_log:
        with open("raw-log.json", mode="w", encoding="utf-8") as f:
            json.dump(response, f, indent=4)
        log_json = []
        for i in range(len(response["results"])):
            log_json.append(response["results"][i][1]["value"])

        with open("waf-log.json", mode="w", encoding="utf-8") as f:
            f.write("[" + str(', '.join(log_json)) + "]")
        debug_message = "[Debug] A raw log file and the excerpted log file were outputted."
        print("\033[36m" + debug_message + "\033[0m")

    with open("waf-log.csv", mode="w", encoding="utf-8") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_NONE, lineterminator="\n", delimiter="\t")

        if action == "BLOCK":
            for i in range(len(response["results"])):
                message = json.loads(response["results"][i][1]["value"])
                row = str(message["timestamp"]) + "," + \
                    message["terminatingRuleId"] + "," + \
                    message["httpRequest"]["uri"] + "," + \
                    message["httpRequest"]["clientIp"] + "," + \
                    message["httpRequest"]["country"]
                writer.writerow([row])
        elif action == "COUNT":
            for i in range(len(response["results"])):
                message = json.loads(response["results"][i][1]["value"])
                for j in range(len(message["nonTerminatingMatchingRules"])):
                    row = str(message["timestamp"]) + "," + \
                        message["nonTerminatingMatchingRules"][j]["ruleId"] + "," + \
                        message["httpRequest"]["uri"] + "," + \
                        message["httpRequest"]["clientIp"] + "," + \
                        message["httpRequest"]["country"]
                    writer.writerow([row])
        else:
            print("Error: action is invalid")
            sys.exit()
    print("[Info] The WAF log file in CSV format for analysis was outputted.")

    # Calc dates
    s_time = datetime.datetime.fromtimestamp(start_time)
    e_time = datetime.datetime.fromtimestamp(end_time)
    days = (e_time - s_time).days

    # Dump data for creating report

    sheet_music = {
        "start_time": start_time,
        "end_time": end_time,
        "days": days,
        "log_group": log_group,
        "action": action,
    }
    with open(SHEET_MUSIC_FILE, mode="w", encoding="utf-8") as f:
        json.dump(sheet_music, f, indent=2)
    print("[Info] The \"sheet_music.json\" file was created for analysis.")
