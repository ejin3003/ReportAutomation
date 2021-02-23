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
        """Fills null values and sets column types
            dct:{
                column_1: ["col_name", "str or int"],
                column_2: ["col_name", "str or int"],
             ...}"""
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

    def filter_out_rows(self):
        """Filter out a rows with a specific value within designated columns
        dct:{"col_1": "val_1", "col_2": "val_2", ...}"""
        # new_df = self.df.copy()
        for col_name in self.dct:
            values_lst = self.dct[col_name]
            mask = -self.df[col_name].isin(values_lst)
            self.df = self.df[mask]
        print(self.df)
        return self.df


    # def rename_columns(self):
    #     pass


cols = ["Name", "Position", "Status"]
data = [["Erza", "Leader", "Active"], ["Atlas", "Knight", "In-Active"], ["Sepra", "Spy", "Active"]]
df = pd.DataFrame(data, columns=cols)
dct = {"Position": ["Spy"], "Status": ["In-Active"]}
obj_df = AlterDataframe(df, dct)
df = obj_df.filter_out_rows()
