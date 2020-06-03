import pandas as pd


def create_n95_report(dest, df_1, df_2):
    writer = pd.ExcelWriter(dest, engine="xlsxwriter")

    df_1.to_excel(writer, sheet_name="CS N95 Report")
    df_2.to_excel(writer, sheet_name="Unit Totals")

    workbook = writer.book
    worksheet_1 = writer.sheets["CS N95 Report"]
    worksheet_1.set_column("A:A", 14)
    worksheet_1.set_column("B:C", 30)
    worksheet_1.set_column("D:F", 14)

    worksheet_2 = writer.sheets["Unit Totals"]
    worksheet_2.set_column("A:A", 30)
    worksheet_2.set_column("B:B", 14)

    writer.save()
    writer.close()


def create_raw_report(dest, df):
    writer = pd.ExcelWriter(dest, engine="xlsxwriter")
    df.to_excel(writer, sheet_name="Unit Totals")

    workbook = writer.book
    worksheet = writer.sheets["Unit Totals"]
    worksheet.set_column("A:A", 14)
    worksheet.set_column("B:C", 30)
    worksheet.set_column("D:F", 14)
    writer.save()
    writer.close()
