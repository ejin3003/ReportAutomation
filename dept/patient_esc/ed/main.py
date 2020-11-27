import pandas as pd


def main():
    """
    Ed Radiology Transport Data: Summary of number of escorts
    """
    pass


df = pd.read_excel(r"C:\Users\jt883\Desktop\ed 11.26.20.xlsx")

# Removes all of the canceled transports
mask_1 = df["Status"] != "Canceled"
df = df[mask_1]

# Selects all of the transports under the "MGH ED Radiology & MGH RAD XRAY ER WH1" Sector
sector_list = ["MGH ED Radiology", "MGH RAD XRAY ER WH1"]
df = df[df["Sector"].isin(sector_list)]

# Converts designated string columns into number columns
# df["Ack->Cmp"] = df["Ack->Cmp"].str.extract(r'(\d*\.?\d*)', expand=False).astype(int)
# df["Ack->InP"] = df["Ack->InP"].str.extract(r'(\d*\.?\d*)', expand=False).astype(int)

col_lst = ["Ack->Cmp", "Ack->InP"]

for num in range(len(col_lst)):
    col = col_lst[num]
    df[col] = df[col].str.extract(r'(\d*\.?\d*)', expand=False).astype(int)

# print("Destination Dept: " + str(df["Destination Department"].nunique()))
# print("Pick-Up Dept: " + str(df["Pick-Up Department"].nunique()))
# print(df.count())
