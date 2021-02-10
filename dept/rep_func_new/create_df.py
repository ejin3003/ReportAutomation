import pandas as pd


class CreateDataframe:
    """Class Functions built to create Pandas dataframes"""
    def __init__(self, path, header_num=0):
        self.path = path
        self.header_num = header_num

    def excel_to_df(self):
        # Creates a pandas dataframe from an excel file
        try:
            filepath = self.path
            df = pd.read_excel(filepath, header=self.header_num)
        except FileNotFoundError:
            msg_error = f"File was not found within specified filepath: {self.path}"
            print(msg_error)
        else:
            print(type(df))
            return df
