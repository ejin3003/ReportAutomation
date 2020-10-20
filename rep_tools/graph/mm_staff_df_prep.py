import pandas as pd

mm_staff_csv = r"C:\Users\jt883\Desktop\PHR_MGH_HR_MAT_MGMT_EE_LIST.csv"
badge_id_xlsx = r"C:\Users\jt883\Desktop\MGH BADGES.xlsx"
pd.set_option("display.width", 400)
pd.set_option("display.max_columns", None)

mm_staff_df = pd.read_csv(mm_staff_csv)
mgh_badge_df = pd.read_excel(badge_id_xlsx)

mgh_badge_df = mgh_badge_df[["Employee ID", "Badge ID"]]

mm_staff_df = mm_staff_df.set_index("ID").join(mgh_badge_df.set_index("Employee ID"))
mm_staff_df.reset_index(inplace=True)
selected_columns = ["index", "Badge ID", "User", "Last", "First Name", "Sex", "Pay Status", "Dept ID", "Dept",
                    "Work Group", "Job Code", "Job Title", "Shift", "Reg/Temp", "Stnd Hrs/Wk", "FTE",
                    "Email ID", "Location"]
mm_staff_df = mm_staff_df[selected_columns]
mm_staff_df.columns = ["id", "badge_id", "username", "last_name", "first_name", "gender", "pay_status", "dept_id",
                       "dept_name", "work_group", "job_code", "job_title", "shift", "reg_temp", "standard_hrs",
                       "fte", "email", "location"]

mm_staff_df.set_index("id", inplace=True)
mm_staff_df.to_excel(r"C:\Users\jt883\Desktop\MM Staff.xlsx")
# print(mm_staff_df.head(3))
# print(mm_staff_df.info())

