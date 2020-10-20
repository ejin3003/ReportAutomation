import pandas as pd


class DataFrameSnsGraph:
    """
    Creates a DataFrame for an SeaBorn Graph
    Parameters: (DataFrame, Sort_Bool, List_Col)
    Example: (df, "Date", True, ["column name"]
    """
    def __init__(self, df, group_col, sort_bool, list_col, test):
        self.df = df
        self.group_col = group_col
        self.sort_bool = sort_bool
        self.list_col = list_col
        self.test = test

    def create_size_sns_df(self):
        group_by_obj = self.df.groupby(self.group_col)
        alter_obj = group_by_obj.size().sort_values(ascending=self.sort_bool)
        df = pd.DataFrame(alter_obj)
        df.columns = self.list_col
        return df

    def create_mean_sns_df(self):
        group_by_obj = self.df.groupby(self.group_col)
        alter_obj = group_by_obj[self.test].mean().sort_values(ascending=self.sort_bool)
        df = pd.DataFrame(alter_obj)
        df.columns = self.list_col
        return df
    # # df_escort_avg: Creates a DataFrame of each escorts average completion time
    # df_escort_avg = escorts["Asgn->Cmp"].mean().sort_values(ascending=True)
    # df_escort_avg = pd.DataFrame(df_escort_avg)
    # df_escort_avg.columns = ["Escort Averages"]
