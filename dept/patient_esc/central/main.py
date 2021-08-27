from dept.rep_func_new.extract_data import ExtractData
from dept.rep_func_new.create_df import CreateDataframe
from dept.rep_func_new.alter_df import AlterDataframe
from dept.rep_func_new.alter_df import JoinTwoDataframes
from dept.rep_func_new.sql_upload import connect, single_insert
from dept.rep_func_new.sql import SequelQuery
# from dept.decorators.timers_func import timer
# from dept.decorators.timers_func import runtime
import pandas as pd

"""
Produces an excel file from EPIC data for the dept. Tableau Dashboard.
"""
# Work: File Paths
path_act_rep = r"\\Cifs2\mghmmprj$\Admin Folders\Jason Tyson\Python\EPIC\Escort Data\Act Reps\Act Rep Feb 2021.xlsx"
path_prd_rep = r"\\Cifs2\mghmmprj$\Admin Folders\Jason Tyson\Python\EPIC\Escort Data\Prod Reps\Prod Rep Feb 2021.xlsx"
dest_file = r"C:\Users\jt883\Desktop\Prod Extract Feb 2021.xlsx"

# Preps EPIC's: Productivity Report Dataframe
df_prod_rep = CreateDataframe(path_prd_rep, header_num=1).excel_to_df()
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 400)
prod_df = ExtractData(df_prod_rep).extract_prod()

# Preps EPIC's: Activity Report Dataframe
raw_act_df = CreateDataframe(path_act_rep).excel_to_df()
filter_dct = {"Status": ["Canceled"]}
act_df = AlterDataframe(raw_act_df).filter_out_rows(filter_dct)

# Creates a new df that extracts the unique values from "Assigned To" & "Assigned To Id in the prod. report
cols_lst = ["Assigned To", "Assigned To ID"]
escort_df = AlterDataframe(act_df).build_unique_df(cols_lst)

# Joins the prod_df & escort_df
prod_df_extracted = JoinTwoDataframes([prod_df, "Transporter"], [escort_df, "Assigned To"]).join_df()

# Fill null values and set column types
num_cols_dct = {
    "Completed": "int",
    "Canceled": "int",
    "Outliers": "int",
    "Escalations": "int",
    "Delay Time": "int",
    "Ack -> In P": "int",
    "In P -> Comp": "int",
    "Ack -> Comp": "int",
    "Total Patient": "int",
    "Total Non-Patient": "int",
    "Assigned To ID": "int"
}
final_prod_df = AlterDataframe(prod_df_extracted).fill_null_set_type(num_cols_dct)
final_prod_df.to_excel(dest_file)

# Upload data to Local PostgreSql Database
column_dict = {
    "fullname": "str",
    "Completed": "int",
    "Canceled": "int",
    "Outliers": "int",
    "Escalations": "int",
    "Delay Time": "int",
    "Ack -> In P": "int",
    "In P -> Comp": "int",
    "Ack -> Comp": "int",
    "Total Patient": "int",
    "Total Non-Patient": "int",
    "Assigned To ID": "int"
}
query_obj = SequelQuery(final_prod_df)
query_list = query_obj.build_query_list(column_dict)
param_dict = {
    "host": "localhost",
    "database": "epic_data",
    "user": "postgres",
    "password": "mgh3003"
}
for query in query_list:
    conn = connect(param_dict)
    single_insert(conn, query)
    conn.close()


