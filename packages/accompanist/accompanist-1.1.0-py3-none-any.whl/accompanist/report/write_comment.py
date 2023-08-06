import json
import matplotlib.patches as patches

CONFIG_FILE = "config.json"
JP_FONT = "YuGothic"


def write_comment(fig):
    """
    Add comment page (last page)
    """
    with open(CONFIG_FILE, mode="r") as f:
        config_dict = json.load(f)

    fig.text(0.091, 0.74, "Comment", color="black", fontsize=20, fontweight="bold")

    fig.subplots_adjust(top=0.7, left=0.09, right=0.98, bottom=0.14, hspace=0.1)
    ax = fig.add_subplot(1, 1, 1)
    ax.axis("off")
    r = patches.Rectangle(xy=(0, 0), width=1, height=1, ec="#ffffff", fc="#eeeeee",
                          linewidth=0, fill=True)
    ax.add_patch(r)

    comment_item = []
    for i in range(len(config_dict["comment"])):
        if i < 6:
            comment_item.append(config_dict["comment"][i])
            y_pos = 0.9 - 0.16 * i
            ax.text(0.02, y_pos, "-", color="black", fontsize=18,
                    va="top", ha="left", wrap=True)
            ax.text(0.04, y_pos, comment_item[i], color="black", fontsize=18,
                    va="top", ha="left", fontfamily=JP_FONT, wrap=True)
        else:
            warning = "[Warning] Some commnets can't be shown because the number of comments may be exceeded."
            print("\033[33m" + warning + "\033[0m")

    note = "[Note] You can add comments optionally in the above area with editing \"sheet_music.json\"."
    ax.text(0.1, -0.06, note, color="black", fontsize=12)
