import pandas as pd

df = pd.read_excel(r"C:\Users\jt883\Desktop\prod_data 12.13 to 12.26.xlsx")

mask = df["Unnamed: 1"] == "Non-patient"
new_df = df[mask]
print(new_df.head())
# mask = df[]



