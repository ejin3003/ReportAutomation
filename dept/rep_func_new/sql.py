

class ConnectSQL:
    def __init__(self, login_dct):
        self.login_dct = login_dct

    def connect(self):
        """Connects to local SQL database."""
        pass


class OperationsSQL(ConnectSQL):
    def __init__(self, df, login_dct):
        super().__init__(login_dct)
        self.df = df

    def fill_missing_values(self):
        """References the designated sql table to fill missing values within a column"""
        pass

    def upload_data(self):
        """Uploads df data to local sql database."""
        pass

    def monthly_prod_rep(self):
        """Tableau Datasource: Creates a excel of escort productivity for the designated month."""
        pass
