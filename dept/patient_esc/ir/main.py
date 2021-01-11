import pandas as pd
from dept.patient_esc.rep_func import extract_reports

"""
Researching a report focusing on escort transports for "MGH Interventional Radiology"
"""
df = pd.read_excel(r"C:\Users\jt883\Desktop\MGH\EPIC\IR Data\IR Data 12.01.20 - 1.09.21.xlsx")
pd.set_option("display.width", 400)
pd.set_option("display.max_columns", None)

# Exploring Data
# print(df.head(3))
# print(df.columns)

# Filter out the records with a "Destination Department" of "MGH IMG IR ELL2"
# mask = df["Destination Department"] == 'MGH IMG IR ELL2'
# ir_dest_df = df[mask]
# print(ir_dest_df.head(3))

# Filter out the records with a "Sector" of "MGH Interventional Radiology"
# mask = df["Sector"] == 'MGH Interventional Radiology'
# ir_sector_df = df[mask]

# Filter out desired columns
columns = ['Transport Date', 'Transport Time', 'Assigned To', 'Pick-up Location', 'Location', 'Destination', 'Region',
           'Source', 'Ack->Cmp', 'Ack->InP', 'Asgn->Ack', 'Asgn->Cmp', 'InP->Cmp', 'Pnd->Asgn', 'Pnd->Cmp',
           'Total Delay Time', 'Job ID', 'Patient Name', 'Assigned Instant', 'Mode', 'Num of Transporters',
           'Day of Month', 'Transport Type', 'Month', 'Week', 'Assigned To ID', 'Status', 'Pick-Up Department',
           'Destination Department', 'Sector']
ir_sector_df = ir_sector_df[columns]

