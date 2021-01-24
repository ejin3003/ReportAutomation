import pandas as pd
from dept.patient_esc.central.rep_func.extract_reports import ExtractData

# File Paths: EPIC's "Activity Report" & Productivity Report
act_rep_file_path = r"C:\Users\jt883\Desktop\MGH\EPIC\Escort Data\Act Reps\Act Rep Jan 2020.xlsx"
prod_rep_file_path = r"C:\Users\jt883\Desktop\MGH\EPIC\Escort Data\Prod Reps\Prod Rep Jan 2020.xlsx"

# File Destinations:
prod_rep_file_dest = r"C:\Users\jt883\Desktop\MGH\EPIC\Escort Data\Reps Altered\Prod Extract Dec 2020.xlsx"


def main():
    """
    1. Imports Epic's activity activity and productivity data.
    2. Cleans & Filters data as needed
    3. Finds any names escort names present in the activity data and absent from the productivity data
    4. Imports altered data into a "Postgresql Database"
    5. Extracts last months data from database for "Tableau Dashboard"
    """
    # Turns Epic's excel data into pandas dataframes
    prod_rep = ExtractData(prod_rep_file_path)
    prod_df = prod_rep.extract_prod()
    act_rep_df = pd.read_excel(act_rep_file_path)

    # Activity Report: Fill null values and set column types
    act_rep_df["Assigned To ID"].fillna(0, inplace=True)
    act_rep_df["Assigned To ID"] = act_rep_df["Assigned To ID"].astype(int)

    # Activity Report: Filter out canceled records
    mask = act_rep_df["Status"] != "Canceled"
    act_rep_df = act_rep_df[mask]

    # Creates a new df that extracts the unique values from "Assigned To" & "Assigned To Id in the productivity report
    gb_escorts = act_rep_df.groupby("Assigned To ID")
    escort_id = gb_escorts["Assigned To"].unique()
    escort_df = pd.DataFrame(escort_id).reset_index()

    for i in escort_df.index:
        for value in escort_df["Assigned To"][i]:
            string_value = ''.join(value)
            escort_df.at[i, "Assigned To"] = string_value

    escort_df.sort_values(by="Assigned To", inplace=True)
    prod_df.reset_index(inplace=True)
    prod_df_extracted = prod_df.set_index("Transporter").join(escort_df.set_index("Assigned To"))

    # Fill null values
    col_lst = ["Ack -> In P", "In P -> Comp", "Ack -> Comp", "Assigned To ID"]
    for num in range(len(col_lst)):
        col_name = col_lst[num]
        prod_df_extracted[col_name].fillna(0, inplace=True)

    # Set column types
    col_lst_2 = ["Completed", "Canceled", "Outliers", "Escalations", "Delay Time", "Ack -> In P", "In P -> Comp",
                 "Ack -> Comp", "Total Patient", "Total Non-Patient", "Assigned To ID"]
    for num in range(len(col_lst_2)):
        col_name = col_lst_2[num]
        prod_df_extracted[col_name] = pd.to_numeric(prod_df_extracted[col_name], errors='coerce').astype(int)

    prod_df_extracted.to_excel(prod_rep_file_dest)


if __name__ == "__main__":
    main()
