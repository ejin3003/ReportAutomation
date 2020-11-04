from rep_tools.extract.extract_reports import ExtractData


def main():
    """
    Extracts a specified section of data from previous months EPIC SYSTEMS: Excel Productivity Report.
    Exports the Extract Excel Productivity Report to the designated filepath.
    """
    file_path = r"C:\Users\tyson\OneDrive\Desktop\MGH\EPIC\PROD. REPS\Oct 2020 Prod Rep.xlsx"
    file_dest = r"C:\Users\tyson\OneDrive\Desktop\MGH\EPIC\PROD. REPS\Oct 2020 Prod Extract.xlsx"
    df_1 = ExtractData(file_path)
    prod_df_extract = df_1.extract_prod()
    prod_df_extract.to_excel(file_dest)


if __name__ == "__main__":
    main()
