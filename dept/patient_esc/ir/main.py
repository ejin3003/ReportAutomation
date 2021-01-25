import pandas as pd

"""
Researching a report focusing on escort transports for "MGH Interventional Radiology"
"""
df = pd.read_excel(r"C:\Users\jt883\Desktop\MGH\EPIC\IR Data\IR Data 12.01.20 - 1.09.21.xlsx")
pd.set_option("display.width", 400)
pd.set_option("display.max_columns", None)

# Filter out the records with a "Sector" of "MGH Interventional Radiology"
mask = df["Sector"] == 'MGH Interventional Radiology'
ir_sector_df = df[mask]

# Filter out desired columns
columns = ['Transport Date', 'Transport Time', 'Assigned To', 'Pick-up Location', 'Location', 'Destination', 'Region',
           'Source', 'Ack->Cmp', 'Ack->InP', 'Asgn->Ack', 'Asgn->Cmp', 'InP->Cmp', 'Pnd->Asgn', 'Pnd->Cmp',
           'Total Delay Time', 'Job ID', 'Patient Name', 'Assigned Instant', 'Mode', 'Num of Transporters',
           'Day of Month', 'Transport Type', 'Month', 'Week', 'Assigned To ID', 'Status', 'Pick-Up Department',
           'Destination Department', 'Sector']
ir_sector_df = ir_sector_df[columns]

"""
Rushed Code:file:"clean_epic_act_rep.py" Turn into Functions
"""
# Filter out records with a "Status" of "Canceled"
mask = ir_sector_df["Status"] != 'Canceled'
new_df = ir_sector_df[mask]

# Uses a Reg Expression to remove the string from each column and convert the type to int
new_df["Assigned To ID"] = new_df["Assigned To ID"].astype(int)
new_df["Ack->Cmp"] = new_df["Ack->Cmp"].str.extract(r'(\d*\.?\d*)', expand=False).astype(int)
new_df["Ack->InP"] = new_df["Ack->InP"].str.extract(r'(\d*\.?\d*)', expand=False).astype(int)
new_df["Asgn->Ack"] = new_df["Asgn->Ack"].str.extract(r'(\d*\.?\d*)', expand=False).astype(int)
new_df["Asgn->Cmp"] = new_df["Asgn->Cmp"].str.extract(r'(\d*\.?\d*)', expand=False).astype(int)
new_df["InP->Cmp"] = new_df["InP->Cmp"].str.extract(r'(\d*\.?\d*)', expand=False).astype(int)
new_df["Pnd->Asgn"] = new_df["Pnd->Asgn"].str.extract(r'(\d*\.?\d*)', expand=False).astype(int)
new_df["Pnd->Cmp"] = new_df["Pnd->Cmp"].str.extract(r'(\d*\.?\d*)', expand=False).astype(int)
new_df["Total Delay Time"] = new_df["Total Delay Time"].str.extract(r'(\d*\.?\d*)', expand=False).astype(int)

new_df.to_excel(r"C:\Users\jt883\Desktop\MGH\EPIC\IR Data\Alter IR Data 12.01.20 - 1.09.21.xlsx")
