import pandas as pd


class AlterDataframe:
    """Functions designed to make alterations to a Pandas dataframe"""
    def __init__(self, df, dct):
        self.df = df
        self.dct = dct

    def fill_null_set_type(self):
        # Fill all null values within a column and set the columns data type
        pass

    def filter_col_val(self):
        """Filter out a value within a single column"""
        for col_name in self.dct:
            print(col_name)
        pass

    def print_new(self):
        print("NEW")
