import pandas as pd
from datetime import date
from datetime import timedelta


def add_daily_total(path, total):
    n95_daily_totals = pd.read_excel(path)

    n95_daily_totals["Date"] = n95_daily_totals["Date"].dt.date

    yesterday = date.today() - timedelta(days=1)

    df = [{
        "Date": yesterday,
        "Total": total
    }]

    n95_daily_totals = n95_daily_totals.append(df, ignore_index=True)

    n95_daily_totals.set_index(keys="Date", inplace=True)
    n95_daily_totals.sort_index(ascending=False, inplace=True)
    return n95_daily_totals
