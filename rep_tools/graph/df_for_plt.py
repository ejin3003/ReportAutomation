import pandas as pd


class DataFramePltGraph:
    """
    Preps DataFrames for Graphing
    Parameters (DataFrame, 'GroupBy Column or [Columns]')
    """
    def __init__(self, df, group_col, list_col):
        self.df = df
        self.group_col = group_col
        self.list_col = list_col

    def create_totals_df(self):
        group_by_object = self.df.groupby(self.group_col)
        totals_obj = group_by_object.size()
        totals_df = pd.DataFrame(data=totals_obj)
        totals_df.reset_index(inplace=True)
        totals_df.columns = self.list_col
        return totals_df
