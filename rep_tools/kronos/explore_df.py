import pandas as pd

df = pd.read_csv(r"C:\Users\jt883\Desktop\KRONOS\kronos_test.csv")
pd.set_option("display.width", 400)
pd.set_option("display.max_columns", None)

selected_columns = df[["EMPID", "USERNAME", "LAST_NAME", "FIRST_NAME", "WEEK_ENDING", "DATE", "HOME_DEPT",
                       "REG_HOURS", "OT_HOURS", "DT_HOURS", "EVE_DIFF", "NIGHT_DIFF", "WKND_DIFF", "OTH_HOURS",
                       "OTH_PAYCODE", "SHIFT_START", "SHIFT_END", "SCHED_START", "SCHED_END", "IN_PUNCH_BY",
                       "OUT_PUNCH_BY", "ET_BALANCE", "ESL_BALANCE", "STD_HOURS", "SCHED_PATTERN", "HOME_ACCT"]]

# Filters out Materials Management Departments
dept_list = ["Patient Transport Service", "Laundry And Linen", "Material Coordination", "Dist Mail Package-Main",
             "Mail Services", "Matls Mgmt Bldg 149", "Materials Management Admin"]
mask = selected_columns["HOME_DEPT"].isin(dept_list)
filtered_selected_columns = selected_columns[mask]

print(selected_columns.head(3))
