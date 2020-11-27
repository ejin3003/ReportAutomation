import pandas as pd
pd.set_option("display.width", 400)
pd.set_option("display.max_columns", None)

# Import Epic Productivity Report
extract_rep = r"C:\Users\tyson\OneDrive\Desktop\MGH\EPIC\PROD. REPS\Oct 2020 Prod Extract.xlsx"
extract_df = pd.read_excel(extract_rep)

# Import Extracted Epic Activity Report
act_rep = r"C:\Users\tyson\OneDrive\Desktop\MGH\EPIC\ACT. REPS\Oct 2020 Act Rep.xlsx"
df = pd.read_excel(act_rep)

# Fill null values and set column types
df["Assigned To ID"].fillna(0, inplace=True)
df["Assigned To ID"] = df["Assigned To ID"].astype(int)

# Filter out canceled records from epic activity report
mask = df["Status"] != "Canceled"
df = df[mask]

# Creates a new df that extracts the unique values from "Assigned To" & "Assigned To Id in the productivity report
gb_escorts = df.groupby("Assigned To ID")
escort_id = gb_escorts["Assigned To"].unique()
escort_df = pd.DataFrame(escort_id).reset_index()


for i in escort_df.index:
    for value in escort_df["Assigned To"][i]:
        string_value = ''.join(value)
        escort_df.at[i, "Assigned To"] = string_value

escort_df.sort_values(by="Assigned To", inplace=True)
new_extract_rep = extract_df.set_index("Transporter").join(escort_df.set_index("Assigned To"))

# Fill null values
new_extract_rep["Ack -> In P"].fillna(0, inplace=True)
new_extract_rep["In P -> Comp"].fillna(0, inplace=True)
new_extract_rep["Ack -> Comp"].fillna(0, inplace=True)
new_extract_rep["Assigned To ID"].fillna(0, inplace=True)

# Set column types
new_extract_rep["Completed"] = new_extract_rep["Completed"].astype(int)
new_extract_rep["Canceled"] = new_extract_rep["Canceled"].astype(int)
new_extract_rep["Outliers"] = new_extract_rep["Outliers"].astype(int)
new_extract_rep["Escalations"] = new_extract_rep["Escalations"].astype(int)
new_extract_rep["Delay Time"] = new_extract_rep["Delay Time"].astype(int)
new_extract_rep["Ack -> In P"] = new_extract_rep["Ack -> In P"].astype(int)
new_extract_rep["In P -> Comp"] = new_extract_rep["In P -> Comp"].astype(int)
new_extract_rep["Ack -> Comp"] = new_extract_rep["Ack -> Comp"].astype(int)
new_extract_rep["Total Patient"] = new_extract_rep["Total Patient"].astype(int)
new_extract_rep["Total Non-Patient"] = new_extract_rep["Total Non-Patient"].astype(int)
new_extract_rep["Assigned To ID"] = new_extract_rep["Assigned To ID"].astype(int)

new_extract_rep.to_excel(r"C:\Users\tyson\OneDrive\Desktop\Oct 2020 Prod Alter.xlsx")
