import pandas as pd


class AlterDataframe:
    """
    Functions designed to make alterations to a Pandas dataframe
    df(Dataframe), dct(dictionary)
    """
    def __init__(self, df, dct):
        self.df = df
        self.dct = dct

    def fill_null_set_type(self):
        """df:Dataframe, dct:{column_1: ["col_1_name", "col_1_type"], ...}"""
        for col in self.dct:
            col_name = self.dct[col][0]
            col_type = self.dct[col][1]
            if col_type == "str":
                self.df[col_name].fillna("Unknown", inplace=True)
                self.df[col_name] = self.df[col_name].astype(str)
            elif col_type == "int":
                self.df[col_name].fillna(0, inplace=True)
                self.df[col_name] = self.df[col_name].astype(int)
        return self.df

    def filter_col_val(self):
        """Filter out a value within a single column"""
        for col_name in self.dct:
            print(col_name)
        pass

    def rename_columns(self):
        pass


