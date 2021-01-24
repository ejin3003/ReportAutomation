

# --------------------------------------------- #
# Testing Extracting MGH: Budget Data
# --------------------------------------------- #
budget_path = r"C:\Users\tyson\OneDrive\Desktop\Budget\Revenue & Expense Aug Detail.xlsx"

extract = ExtractData(budget_path)
extract_df = extract.extract_excel_section()
extract_df = extract_df.iloc[6:108, :11]
extract_df.columns = ['Section', 'Category', 'MTD Actual', 'MTD Budget', 'MTD Variance', 'MTD Var %', 'YTD Actual',
                      'YTD Budget', 'YTD Variance', 'YTD Var %', 'Annual Budget']

category_list = ["Other Revenue", "Operating Revenue", "Benefits", "Supplies", "Utilities", "Space Related Costs",
                 "Equipment Related Expense", "Other", "Depreciation and Amortization", "Interest",
                 "Operating Expenses"]

for i in extract_df["Section"]:
    if i in category_list:
        print(i, extract_df[extract_df["Section"] == i].index.values)
