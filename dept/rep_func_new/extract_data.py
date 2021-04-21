import datetime
import calendar


class ExtractData:
    """
    Functions designed to extract specific data from epic excel reports
    """
    def __init__(self, df):
        self.df = df

    def extract_prod(self):
        # Epic's Productivity Excel Report: Extracts a specific section summarized data
        # Potential Tests: File Exists, Function returns a pandas dataframe
        target_row = 0
        for row in range(self.df.shape[0]):
            if self.df.at[row, "Transporter"] == "Average":
                target_row = row
                break
        new_df = self.df.iloc[:target_row]
        new_df = new_df.set_index("Transporter")
        now = datetime.datetime.now().month
        month_name = calendar.month_name[now - 1]
        new_df["Month"] = month_name
        new_df.reset_index(inplace=True)
        return new_df
