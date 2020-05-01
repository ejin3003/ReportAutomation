import pandas as pd
from openpyxl import load_workbook
from datetime import date
from datetime import timedelta


def add_daily_total(path, dest, ref):
    n95_daily_totals = pd.read_excel(path)
    df = pd.read_excel(ref)

    n95_daily_totals["Date"] = n95_daily_totals["Date"].dt.date

    total = df["Qty"].sum()
    yesterday = date.today() - timedelta(days=1)

    df = [{
        "Date": yesterday,
        "Total": total
    }]

    n95_daily_totals = n95_daily_totals.append(df, ignore_index=True)

    n95_daily_totals.set_index(keys="Date", inplace=True)
    n95_daily_totals.sort_index(ascending=False, inplace=True)
    # print(n95_daily_totals)

    # Add Daily Total to the N95 Report
    writer = pd.ExcelWriter(dest, engine="openpyxl")
    book = load_workbook(dest)
    writer.book = book
    n95_daily_totals.to_excel(writer, sheet_name="Daily Totals")
    sheet = book.get_sheet_by_name("Daily Totals")
    sheet.column_dimensions["A"].width = 14
    sheet.column_dimensions["B"].width = 14
    writer.save()
    writer.close()
