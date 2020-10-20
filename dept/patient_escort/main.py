from extract.extract_reports import ExtractData

# Extracts a specified section of data from previous months EPIC SYSTEMS: Excel Productivity Report
file_path = r"C:\Users\tyson\OneDrive\Desktop\Sept 17 2020 Prod Rep.xlsx"
df_1 = ExtractData(file_path)
prod_df_extract = df_1.extract_prod()

# Exports the Extract Excel Productivity Report to the designated filepath


