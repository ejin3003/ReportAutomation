import pandas as pd
import datetime
import calendar


class ExtractData:
    """
    Functions designed to extract specific data from epic excel reports
    """
    def __init__(self, path):
        self.path = path

    def extract_prod(self):
        df = pd.read_excel(self.path, header=1)
        pd.set_option("display.width", 400)
        pd.set_option("display.max_columns", None)

        target_row = 0
        for row in range(df.shape[0]):
            if df.at[row, "Transporter"] == "Average":
                # print(row, "Transporter")
                target_row = row
                break
        new_df = df.iloc[:target_row]
        new_df = new_df.set_index("Transporter")
        now = datetime.datetime.now().month
        month_name = calendar.month_name[now - 1]
        # month_name = "desired month"
        new_df["Month"] = month_name
        return new_df

    def extract_excel_section(self):
        """
        Extracts specified rows and columns within the designated excel file, returns a dataframe
        """
        df = pd.read_excel(self.path)

        return df


############################################
# Testing Extracting MGH: Budget Data
############################################

# budget_path = r"C:\Users\tyson\OneDrive\Desktop\Budget\Revenue & Expense Aug Detail.xlsx"
#
# extract = ExtractData(budget_path)
# extract_df = extract.extract_excel_section()
# extract_df = extract_df.iloc[6:108, :11]
# extract_df.columns = ['Section', 'Category', 'MTD Actual', 'MTD Budget', 'MTD Variance', 'MTD Var %', 'YTD Actual',
#                       'YTD Budget', 'YTD Variance', 'YTD Var %', 'Annual Budget']
#
# category_list = ["Other Revenue", "Operating Revenue", "Benefits", "Supplies", "Utilities", "Space Related Costs",
#                  "Equipment Related Expense", "Other", "Depreciation and Amortization", "Interest",
#                  "Operating Expenses"]
#
# for i in extract_df["Section"]:
#     if i in category_list:
#         print(i, extract_df[extract_df["Section"] == i].index.values)
