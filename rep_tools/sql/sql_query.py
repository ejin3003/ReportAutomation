import pandas as pd
import pandas.io.sql as sqlio
import psycopg2
from rep_tools.sql.sql_upload import connect
pd.set_option("display.width", 400)
pd.set_option("display.max_columns", None)

params_dict = {
    "host": "localhost",
    "database": "epic_data",
    "user": "postgres",
    "password": "mgh3003"
}
conn = connect(params_dict)
# sql = "SELECT * FROM prod_data;"
# sql = "SELECT month, SUM(completed) FROM prod_data " \
#       "GROUP BY month;"
# sql = "SELECT last_name, first_name, dept_name FROM mm_staff " \
#       "WHERE dept_name = 'Patient Transport (Day)'" \
#       "OR dept_name = 'Pt Transport, Equip & Ofc Svcs'" \
#       "OR dept_name = 'Materials Mgt Customer Service'" \
#       "ORDER BY last_name;"
sql = "SELECT pr.fullname, pr.completed, pr.canceled, pr.escalations, pr.delay_time, pr.ack_inp, pr.inp_comp, " \
      "ack_comp, working_time, idle_time, break_time, work_days, total_patient, total_non_patient, month, " \
      "mm.shift FROM prod_data pr " \
      "INNER JOIN mm_staff mm ON pr.epic_id = mm.epic_id " \
      "WHERE pr.month = 'March';"

df = sqlio.read_sql_query(sql, conn)
conn.close()

print(df.head(3))
df.set_index('fullname', inplace=True)
df.to_excel(r"C:\Users\jt883\Desktop\Prod SQL Alter Mar 2021.xlsx")
# Don't forget to change the SQL query month !!!

