from rep_tools.read.read_reports import ReadReports


# def main():
#     """
#     Weekly N95 Report: Produces an excel report which displays the quantity of "N95 Mask" ordered by unit for the past
#     7 days.
#     """
#     path = r"C:\Users\jt883\Desktop\N95 Report.xlsx"
#
#     df_obj = ReadReports(path)
#     df = df_obj.import_report()
#     print(df.head())
#
#
# if __name__ == "__main__":
#     main()


path = r"C:\Users\jt883\Desktop\N95 Report.xlsx"

df_obj = ReadReports(path)
df = df_obj.import_report()
print(df.head())
