import pandas as pd

# Exploring Epic Department Data/Report

df = pd.read_excel(r"C:\Users\jt883\Desktop\Test Sept 2020 Rep.xlsx")

dept_df = pd.Series(df["Pick-Up Department"].unique()).sort_values()

dept_grb = df.groupby("Pick-Up Department")
dept_count_df = dept_grb["Status"].count().sort_values(ascending=False)
