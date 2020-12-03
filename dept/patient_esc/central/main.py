import pandas as pd
from dept.patient_esc.central.rep_func.extract_reports import ExtractData


def main():
    """
    Extracts a specified section of data from previous months EPIC SYSTEMS: Excel Productivity Report.
    Exports the Extract Excel Productivity Report to the designated filepath.
    """
    prod_rep_file_path = r"C:\Users\tyson\OneDrive\Desktop\MGH\EPIC\PROD. REPS\Prod Rep Nov 2020.xlsx"
    act_rep_file_path = r"C:\Users\tyson\OneDrive\Desktop\MGH\EPIC\ACT. REPS\Act Rep Nov 2020.xlsx"
    # prod_rep_file_dest = r"C:\Users\tyson\OneDrive\Desktop\MGH\EPIC\PROD. REPS\Prod Extract Nov 2020.xlsx"
    prod_rep_file_dest = r"C:\Users\tyson\OneDrive\Desktop\Prod Extract Nov 2020.xlsx"

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
    prod_df_extracted["Ack -> In P"].fillna(0, inplace=True)
    prod_df_extracted["In P -> Comp"].fillna(0, inplace=True)
    prod_df_extracted["Ack -> Comp"].fillna(0, inplace=True)
    prod_df_extracted["Assigned To ID"].fillna(0, inplace=True)


    # Set column types
    # prod_df_extracted["Completed"] = prod_df_extracted["Completed"]
    prod_df_extracted["Completed"] = pd.to_numeric(prod_df_extracted["Completed"], errors='coerce').astype(int)
    # prod_df_extracted["Canceled"] = prod_df_extracted["Canceled"].astype(int)
    prod_df_extracted["Canceled"] = pd.to_numeric(prod_df_extracted["Canceled"], errors='coerce').astype(int)
    # prod_df_extracted["Outliers"] = prod_df_extracted["Outliers"].astype(int)
    prod_df_extracted["Outliers"] = pd.to_numeric(prod_df_extracted["Outliers"], errors='coerce').astype(int)
    # prod_df_extracted["Escalations"] = prod_df_extracted["Escalations"].astype(int)
    prod_df_extracted["Escalations"] = pd.to_numeric(prod_df_extracted["Escalations"], errors='coerce').astype(int)
    # prod_df_extracted["Delay Time"] = prod_df_extracted["Delay Time"].astype(int)
    # prod_df_extracted["Ack -> In P"] = prod_df_extracted["Ack -> In P"].astype(int)
    # prod_df_extracted["In P -> Comp"] = prod_df_extracted["In P -> Comp"].astype(int)
    # prod_df_extracted["Ack -> Comp"] = prod_df_extracted["Ack -> Comp"].astype(int)
    # prod_df_extracted["Total Patient"] = prod_df_extracted["Total Patient"].astype(int)
    # prod_df_extracted["Total Non-Patient"] = prod_df_extracted["Total Non-Patient"].astype(int)
    # prod_df_extracted["Assigned To ID"] = prod_df_extracted["Assigned To ID"].astype(int)

    # prod_df_extracted.to_excel(prod_rep_file_dest)

    # prod_df.to_excel(prod_rep_file_dest)

    print(prod_df_extracted.head())


if __name__ == "__main__":
    main()
