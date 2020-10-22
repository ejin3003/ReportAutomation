import pandas as pd


class AlterColumns:
    """
    Functions designed to alter columns names within a dataframe
    """
    def __init__(self, df, colm_lst):
        self.df = df,
        self.colm_lst = colm_lst

    def alter_colm_names(self):
        """
        1. Checks if the list of column names matches the total number of columns within the dataframe
        2. If list_colm_names = total_df_colm then rename the df colm according to the list

        """
        len_col_lst = len(self.colm_lst)

        df_colm = pd.DataFrame(self.df)
        len_df_colm = len(df_colm.columns)

        print(pd.DataFrame(self.df))
        # print(len_col_lst)
        # print(len_df_colm)




