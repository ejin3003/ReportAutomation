import pandas as pd


class ReadReports:
    """
    Functions designed to read existing excel reports
    """

    def __init__(self, path):
        self.path = path

    def import_report(self):
        rep = pd.read_excel(self.path)
        pd.set_option("display.width", 400)
        pd.set_option("display.max_columns", None)
        return rep


