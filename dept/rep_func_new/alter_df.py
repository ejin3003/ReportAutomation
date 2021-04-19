import pandas as pd


class AlterDataframe:
    """
    Functions designed to make alterations to a Pandas dataframe
    df(Dataframe), dct(dictionary)
    """
    def __init__(self, df):
        self.df = df

    def fill_null_set_type(self, dct):
        """Fills null values and sets column types
            dct:{
                "col_name", "str or int",
                 ...}
             """
        for _, k in enumerate(dct):
            val = dct[k]
            if val == "str":
                self.df[k].fillna("Unknown", inplace=True)
                self.df[k] = self.df[k].astype(str)
            elif val == "int":
                self.df[k].fillna(0, inplace=True)
                self.df[k] = self.df[k].astype(int)
        return self.df

    def filter_out_rows(self, dct):
        """Filter out a rows with a specific value within designated columns
        dct:{"col_1": "val_1", "col_2": "val_2", ...}"""
        # new_df = self.df.copy()
        for col_name in dct:
            values_lst = dct[col_name]
            mask = -self.df[col_name].isin(values_lst)
            self.df = self.df[mask]
        return self.df

    def build_unique_df(self, lst):
        """Creates a dataframe that contains the unique values from two columns"""
        col_1, col_2 = lst[0], lst[1]
        gb_obj = self.df.groupby(col_1)
        unique_series = gb_obj[col_2].unique()  # 2nd col is a list of unique values
        new_df = pd.DataFrame(unique_series).reset_index()
        new_df[col_2] = new_df[col_2].map(lambda x: x[0])  # Takes the first value from the list
        return new_df

    def join_dataframes(self, join_df, lst):
        """ Joins two dataframes lst = ["col_name_1", "col_name_2]"""
        join_1, join_2 = lst[0], lst[1]
        joined_df = self.df.set_index(join_1).join(join_df.set_index(join_2))
        # new = joined_df.set_index(join_1)
        return joined_df

# Testing
# cols_1, cols_2 = ["Name", "ID"], ["ID", "Shift"]
# data_1, data_2 = [["Erza", 1], ["Ejin", 3], ["Sepra", 2]], [[2, "Evening"], [3, "Day"], [1, "Night"]]
# df_1, df_2 = pd.DataFrame(data_1, columns=cols_1), pd.DataFrame(data_2, columns=cols_2)
# join_lst = ["ID", "ID"]
# joined_df = AlterDataframe(df_1).join_dataframes(df_2, join_lst)
# joined_df = joined_df.set_index("Name")
# print(joined_df)
# lst_df = joined_df.values.tolist()
