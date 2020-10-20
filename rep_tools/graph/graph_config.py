
def graph_daily_trip_totals(df_daily_totals):
    import pandas as pd
    import matplotlib.pyplot as plt

    x = df_daily_totals["Date"].to_list()
    y = df_daily_totals["Daily Total"].to_list()

    plt.figure(figsize=(10, 6), dpi=300)

    plt.style.use("ggplot")
    plt.plot(x, y, label="Total Escorts", linewidth=2, marker=".", markersize=6)

    plt.title("Completed Central Trips for the Month of June", fontdict={"fontsize": 20})
    plt.xlabel("April 2020", fontdict={"fontsize": 14})
    plt.xticks(rotation=45)
    plt.ylabel("Total Trips", fontdict={"fontsize": 14})

    plt.legend()
    plt.show()


def graph_escort_totals(df_escort_totals):
    import matplotlib.pyplot as plt
    plt.figure(figsize=(20, 12), dpi=300)
    plt.style.use("seaborn-deep")
    df_escort_totals.plot(kind="barh", figsize=(18, 16), width=.85, fontsize=14)
    plt.gca().invert_yaxis()
    plt.title("Completed Escort Totals for the Month of June", fontdict={"fontsize": 20})
    plt.xlabel("April: Total Trips", fontdict={"fontsize": 14})
    plt.xticks(rotation=45)
    plt.ylabel("Escort", fontdict={"fontsize": 14})
    plt.legend()
    plt.show()


def sns_bar_plot(df_escort_totals):
    import matplotlib.pyplot as plt
    import seaborn as sns
    x = df_escort_totals["Escort Total"]
    y = df_escort_totals.index
    # Options Color Palette's >> "Blues_d", "plasma", "summer"
    sns.set(rc={"figure.figsize":(14, 20)})
    ax = sns.barplot(x, y, data=df_escort_totals, palette="plasma")
    ax.set_title("April: Completed Trips Total")
    initialx = 0
    for p in ax.patches:
        ax.text(p.get_width(), initialx + p.get_height()/8, "{:1.0f}".format(p.get_width()))
        initialx += 1
    plt.show()
