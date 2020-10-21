from rep_tools.z_misc.n95_rep_tools.rename_report_cells import *
from rep_tools.z_misc.n95_rep_tools.unit_totals import *
from rep_tools.z_misc.n95_rep_tools.append_to_df import *
from rep_tools.z_misc.n95_rep_tools.rep_xlsxwriter import *
from datetime import date
from datetime import timedelta

yesterday = date.today() - timedelta(days=1)

# Work File Paths & Destinations
n95_report_path = r"C:\Users\jt883\Desktop\N95 Report.xlsx"
unit_total_path = r"C:\Users\jt883\Desktop\Raw CS Data N95.xlsx"
daily_totals_path = r"C:\Users\jt883\Desktop\N95 Daily Totals.xlsx"
n95_report_dest = r"C:\Users\jt883\Desktop\CS N95 Report {}.xlsx".format(yesterday)
raw_report_dest = r"C:\Users\jt883\Desktop\Raw CS Data N95 {}.xlsx".format(yesterday)

# Home File Paths & Destinations
# n95_report_path = r"C:\Users\ejin3\OneDrive\Desktop\N95 Report.xlsx"
# unit_total_path = r"C:\Users\ejin3\OneDrive\Desktop\Raw CS Data N95.xlsx"
# n95_report_dest = r"C:\Users\ejin3\OneDrive\Desktop\CS N95 Report {}.xlsx".format(yesterday)
# daily_totals_path = r"C:\Users\ejin3\OneDrive\Desktop\N95 Daily Totals.xlsx"

# Creates DataFrames for the N95 Report
n95_rep_df = rename_n95_report(n95_report_path)
unit_report_df, unit_total_df, total = unit_totals(unit_total_path)
daily_totals_df = add_daily_total(daily_totals_path, total)

# Create Reports
create_n95_report(n95_report_dest, n95_rep_df, unit_total_df, daily_totals_df)
create_raw_report(raw_report_dest, unit_report_df)
create_daily_totals_ref(daily_totals_path, daily_totals_df)

