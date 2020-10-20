def clean_act_rep(path):
    import pandas as pd

    df = pd.read_excel(path, parse_dates=["Transport Date"])
    pd.set_option("display.max_columns", None)
    df["Pick-up Location"].fillna("None", inplace=True)
    df["Mode"].fillna("None", inplace=True)

    # Filters out all canceled trips
    mask = df["Status"] != "Canceled"
    df = df[mask]

    # Filters out designated escorts
    mask_escort = df["Assigned To"] != "EDRadTransporter, Two"
    df = df[mask_escort]

    # Uses a Reg Expression to remove the string from each column and convert the type to int
    df["Assigned To ID"] = df["Assigned To ID"].astype(int)
    df["Ack->Cmp"] = df["Ack->Cmp"].str.extract(r'(\d*\.?\d*)', expand=False).astype(int)
    df["Ack->InP"] = df["Ack->InP"].str.extract(r'(\d*\.?\d*)', expand=False).astype(int)
    df["Asgn->Ack"] = df["Asgn->Ack"].str.extract(r'(\d*\.?\d*)', expand=False).astype(int)
    df["Asgn->Cmp"] = df["Asgn->Cmp"].str.extract(r'(\d*\.?\d*)', expand=False).astype(int)
    df["InP->Cmp"] = df["InP->Cmp"].str.extract(r'(\d*\.?\d*)', expand=False).astype(int)
    df["Pnd->Asgn"] = df["Pnd->Asgn"].str.extract(r'(\d*\.?\d*)', expand=False).astype(int)
    df["Pnd->Cmp"] = df["Pnd->Cmp"].str.extract(r'(\d*\.?\d*)', expand=False).astype(int)
    df["Total Delay Time"] = df["Total Delay Time"].str.extract(r'(\d*\.?\d*)', expand=False).astype(int)

    # Creates a separate DataFrame with desired columns
    df = df[[
        'Transport Date',
        'Assigned To ID',
        'Assigned To',
        'Ack->Cmp',
        'Ack->InP',
        'Asgn->Ack',
        'Asgn->Cmp',
        'InP->Cmp',
        'Pnd->Asgn',
        'Pnd->Cmp',
        'Total Delay Time'
        ]]
    df["Transport Date"] = df["Transport Date"].dt.date

    return df

    # # df_daily_totals: Creates a DataFrame of the escort's combined daily totals
    # dates = df.groupby('Transport Date')
    # daily_totals = dates.size()
    # df_daily_totals = pd.DataFrame(data=daily_totals)
    # df_daily_totals.reset_index(inplace=True)
    # df_daily_totals.columns = ["Date", "Daily Total"]
    #
    # # df_escort_totals: Creates a DataFrame of total trips per escort
    # escorts = df.groupby("Assigned To")
    # escort_totals = escorts.size().sort_values(ascending=False)
    # df_escort_totals = pd.DataFrame(escort_totals)
    # df_escort_totals.columns = ["Escort Total"]
    #
    # # df_escort_avg: Creates a DataFrame of each escorts average completion time
    # df_escort_avg = escorts["Asgn->Cmp"].mean().sort_values(ascending=True)
    # df_escort_avg = pd.DataFrame(df_escort_avg)
    # df_escort_avg.columns = ["Escort Averages"]
    #
    # # df_escort_ack: Creates a DataFrame of the avg time to acknowledge per escort
    # df_escort_ack = escorts["Asgn->Ack"].mean().sort_values(ascending=False)
    # df_escort_ack = pd.DataFrame(df_escort_ack)
    # df_escort_ack.columns = ["Average Time to Acknowledge"]
    #
    # return df_daily_totals, df_escort_totals, df_escort_avg, df_escort_ack


# path = r"C:\Users\tyson\OneDrive\Desktop\Apr 2020 Act Rep.xlsx"
# path = r"C:\Users\jt883\Desktop\Apr 2020 Act Rep.xlsx"
# df = act_report(path)
