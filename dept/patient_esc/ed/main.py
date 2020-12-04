import pandas as pd


def main():
    """
    Ed Radiology Transport Data: Summary of number of escorts
    """
    pass


df = pd.read_excel(r"C:\Users\jt883\Desktop\ED Act Rep Nov 2020.xlsx")
pd.set_option("display.width", 400)
pd.set_option("display.max_columns", None)

# Removes all of the canceled transports
mask_1 = df["Status"] != "Canceled"
df = df[mask_1]

# Selects all of the transports under the "MGH ED Radiology & MGH RAD XRAY ER WH1" Sector
sector_list = ["MGH ED Radiology", "MGH RAD XRAY ER WH1"]
df = df[df["Sector"].isin(sector_list)]

# Converts designated string columns into number columns
col_lst = ["Ack->Cmp", "Ack->InP", "Asgn->Ack", "Asgn->Cmp", "InP->Cmp", "Pnd->Asgn", "Pnd->Cmp", "Total Delay Time"]
for num in range(len(col_lst)):
    col = col_lst[num]
    df[col] = df[col].str.extract(r'(\d*\.?\d*)', expand=False).astype(int)

# Removes time from "Transport Date" column
df["Transport Date"] = df["Transport Date"].dt.date

print(df.describe())
