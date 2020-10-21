import pandas as pd
from openpyxl import load_workbook
from datetime import date
from datetime import timedelta


def format_report(path):
    writer = pd.ExcelWriter(path, engine="openpyxl")
    book = load_workbook(path)
    writer.book = book

    yesterday = date.today() - timedelta(days=1)
    sheet_1 = f"CS N95 Report {yesterday}"

    sheet = book.get_sheet_by_name(sheet_1)
    sheet.column_dimensions["A"].width = 14
    sheet.column_dimensions["B"].width = 35
    sheet.column_dimensions["C"].width = 35
    sheet.column_dimensions["D"].width = 12
    sheet.column_dimensions["E"].width = 12
    sheet.column_dimensions["F"].width = 12
    writer.save()
    writer.close()
