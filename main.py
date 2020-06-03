from Report_Tools.rename_report_cells import *
from Report_Tools.unit_totals import *
from Report_Tools.format_sheets import *
from Report_Tools.append_to_df import *
from Report_Tools.rep_xlsxwriter import *
from datetime import date
from datetime import timedelta

yesterday = date.today() - timedelta(days=1)

# Renames columns and mask names within the Customer Service N95 Report >> Also appends unit totals to N95 Report
n95_report_path = r"C:\Users\jt883\Desktop\N95 Report.xlsx"
unit_total_path = r"C:\Users\jt883\Desktop\Raw CS Data N95.xlsx"
n95_report_dest = r"C:\Users\jt883\Desktop\CS N95 Report {}.xlsx".format(yesterday)
raw_report_dest = r"C:\Users\jt883\Desktop\Raw CS Data N95 {}.xlsx".format(yesterday)
daily_totals = r"C:\Users\jt883\Desktop\N95 Daily Totals.xlsx"

# Home File Path
# n95_report_path = r"C:\Users\ejin3\OneDrive\Desktop\N95 Report.xlsx"
# unit_total_path = r"C:\Users\ejin3\OneDrive\Desktop\Raw CS Data N95.xlsx"
# n95_report_dest = r"C:\Users\ejin3\OneDrive\Desktop\CS N95 Report {}.xlsx".format(yesterday)
# daily_totals = r"C:\Users\ejin3\OneDrive\Desktop\N95 Daily Totals.xlsx"

# Creates DataFrames for the N95 Report
n95_rep_df = rename_n95_report(n95_report_path)
unit_report_df, unit_total_df = unit_totals(unit_total_path)
# add_daily_total(daily_totals, n95_report_dest, unit_total_path)

# Create Reports
create_n95_report(n95_report_dest, n95_rep_df, unit_total_df)
create_raw_report(raw_report_dest, unit_report_df)
