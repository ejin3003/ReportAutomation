import pandas as pd

# Exploring Epic Department Data/Report

df = pd.read_excel(r"C:\Users\jt883\Desktop\Test Sept 2020 Rep.xlsx")

# Creates a new column with "MGH " stripped from "Pick-Up Department Column"
df["mm_name"] = df["Pick-Up Department"].map(lambda x: x.replace('MGH ', '').upper())

# selected_cols = ["mm_name", "Pick-up Location"]
# dept_df = df[selected_cols]
# new_dept_df = dept_df.drop_duplicates("mm_name")
# new_dept_df = new_dept_df[["mm_name", "Pick-up Location"]].sort_values("mm_name")

dept_series = pd.Series(df["mm_name"].unique()).sort_values()

dept_grb = df.groupby("Pick-Up Department")
dept_count_df = dept_grb["Status"].count().sort_values(ascending=False)
