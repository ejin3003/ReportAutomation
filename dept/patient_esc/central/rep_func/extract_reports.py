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
        """
        Epic's Productivity Excel Report: Extracts a specific section summarized data
        Potential Tests: File Exists, Function returns a pandas dataframe
        """
        df = pd.read_excel(self.path, header=1)
        pd.set_option("display.width", 400)
        pd.set_option("display.max_columns", None)

        target_row = 0
        for row in range(df.shape[0]):
            if df.at[row, "Transporter"] == "Average":
                target_row = row
                break
        new_df = df.iloc[:target_row]
        new_df = new_df.set_index("Transporter")
        now = datetime.datetime.now().month
        month_name = calendar.month_name[now - 1]
        new_df["Month"] = month_name
        return new_df


file_path = r"C:\Users\ejin3\OneDrive\Desktop\Oct 2020 Prod Rep.xlsx"

test_obj = ExtractData(file_path)
extracted_prod_df = test_obj.extract_prod()
print(type(extracted_prod_df))

