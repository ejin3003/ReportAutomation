import pandas as pd

df = pd.read_excel(r"C:\Users\ejin3\OneDrive\Desktop\prod_escort_trans.xlsx")
pd.set_option("display.width", 400)
pd.set_option("display.max_columns", None)

mask = df["Destination"] == "MGH Lab Micro Gray 5"
micro_df = df[mask]

micro_df.to_excel(r"C:\Users\ejin3\OneDrive\Desktop\Epic Specimen Records 12.23.20 to 12.26.20.xlsx")
