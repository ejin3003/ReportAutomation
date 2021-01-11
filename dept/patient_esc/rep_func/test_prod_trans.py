import pandas as pd

# Imports designated "Productivity Report". Sets the second row as the header
df = pd.read_excel(r"C:\Users\ejin3\OneDrive\Desktop\prod_data 12.13 to 12.26.xlsx", header=1)
pd.set_option("display.width", 400)
pd.set_option("display.max_columns", None)

# Extracts escorts totals & averages as a new dataframe
last_row = 0
for row in range(df.shape[0]):
    if df.at[row, "Transporter"] == "Average":
        last_row = row
        break
escort_stats_df = df.iloc[:last_row]
start_row = last_row + 1
misc_df = df.iloc[start_row:]
misc_df.reset_index(inplace=True, drop=True)

# Creates a list of escort names within the "escort_stats_df"
escort_names_lst = list(escort_stats_df["Transporter"])

# Creates a empty dataframe
df_cols = ["Ack Date/Time", "Job Type", "Origin", "Destination", "Priority", "Escalated?", "Was an Assist?",
           "Ack -> In P", "In P -> Comp", "Ack -> Comp", "Delay Time", "Delay Reason", "Canceled?",
           "Outlier?", "Job ID", "Escort"]
final_df = pd.DataFrame()

is_first = 0
escort_name = ""
name_row = 0
end_row = 0
for row in range(misc_df.shape[0]):
    if misc_df.at[row, "Transporter"] in escort_names_lst:
        escort_name = misc_df.at[row, "Transporter"]
        name_row = row
        # print(name_row)
        continue
    if misc_df.at[row, "Transporter"] == "Event Information":
        end_row = row
        # print(end_row)
        temp_df = misc_df.iloc[name_row + 2:end_row]
        temp_df["Escort"] = escort_name
        temp_df.columns = df_cols
        if is_first == 0:
            is_first = 1
            final_df = temp_df.copy()
            continue
        else:
            final_df = final_df.append(temp_df)
        continue

final_df.to_excel(r"C:\Users\ejin3\OneDrive\Desktop\prod_escort_trans.xlsx")
