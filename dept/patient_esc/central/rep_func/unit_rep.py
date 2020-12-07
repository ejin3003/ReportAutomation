import pandas as pd

df = pd.read_excel(r"C:\Users\jt883\Desktop\Act Rep Nov 2020.xlsx")
# print(df["Pick-Up Department"].nunique())
# print(df["Sector"].nunique())

# gb_sector = df.groupby('Sector')
# sector_count_df = gb_sector["Status"].count()
# print(sector_count_df.sort_values(ascending=False))

# Removes all of the canceled transports
mask = df["Status"] != "Canceled"
df = df[mask]

# Converts designated string columns into number columns
col_lst = ["Ack->Cmp", "Ack->InP", "Asgn->Ack", "Asgn->Cmp", "InP->Cmp", "Pnd->Asgn", "Pnd->Cmp", "Total Delay Time"]
for num in range(len(col_lst)):
    col = col_lst[num]
    df[col] = df[col].str.extract(r'(\d*\.?\d*)', expand=False).astype(int)

gb_pkup_dept = df.groupby('Pick-Up Department')
pkup_dept_df = gb_pkup_dept.agg({
    'Pnd->Asgn': 'mean',
    'Pnd->Cmp': 'mean',
    'Asgn->Ack': 'mean',
    'Asgn->Cmp': 'mean',
    'Ack->InP': 'mean',
    'Ack->Cmp': 'mean',
    'Total Delay Time': 'sum',
    'Pick-Up Department': 'count'
})

# pkup_dept_df = pkup_dept_df.sort_values(ascending=False)
