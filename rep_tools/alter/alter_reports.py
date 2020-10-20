
class AlterReport:
    """
    Functions for altering the values within a dataframe
    """
    def __init__(self, df, col, dct):
        self.df = df
        self.col = col
        self.dct = dct

    def replace_col_val(self):
        self.df[self.col].replace(self.dct, inplace=True)
        return self.df


class AddColumn:
    """
    Add a new column with specific values based on a dictionary
    """
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def add_col(self):
        pass
