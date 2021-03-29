from dept.rep_func_new.extract_data import ExtractData
from dept.rep_func_new.create_df import CreateDataframe
from dept.rep_func_new.alter_df import AlterDataframe
from dept.decorators.timers_func import timer
from dept.decorators.timers_func import runtime
import pandas as pd


@timer
def main():
    """
    Produces an excel file from EPIC data for the dept. Tableau Dashboard.
    """
    # File Paths
    path_act_rep = r"C:\Users\ejin3\Documents\MGH\Epic\Act Rep Jan 2021.xlsx"
    path_prd_rep = r"C:\Users\ejin3\Documents\MGH\Epic\Prod Rep Jan 2021.xlsx"
    dest_file = r"C:\Users\ejin3\Documents\MGH\Epic\Prod. Reps\Prod Extract Jan 2021.xlsx"

    # Preps EPIC's: Productivity Report Dataframe
    df_prod_rep = CreateDataframe(path_prd_rep, header_num=1).excel_to_df()
    prod_df = ExtractData(df_prod_rep).extract_prod()

    # Preps EPIC's: Activity Report Dataframe
    raw_act_df = CreateDataframe(path_act_rep).excel_to_df()
    dct_1, dct_2 = {"column_1": ["Assigned To ID", "int"]}, {"Status": ["Canceled"]}
    c_act_df = AlterDataframe(raw_act_df).fill_null_set_type(dct_1)
    act_df = AlterDataframe(c_act_df).filter_out_rows(dct_2)

    # Creates a new df that extracts the unique values from "Assigned To" & "Assigned To Id in the productivity report
    gb_escorts = act_df.groupby("Assigned To ID")
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

    prod_df_extracted.to_excel(dest_file)


if __name__ == '__main__':
    main()
