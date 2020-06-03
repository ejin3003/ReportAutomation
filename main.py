from Report_Tools.rename_report_cells import *
from Report_Tools.unit_totals import *
from Report_Tools.format_sheets import *
from Report_Tools.append_to_df import *
from datetime import date
from datetime import timedelta

yesterday = date.today() - timedelta(days=1)

# Renames columns and mask names within the Customer Service N95 Report >> Also appends unit totals to N95 Report
n95_report_path = r"C:\Users\jt883\Desktop\N95 Report.xlsx"
unit_total_path = r"C:\Users\jt883\Desktop\Raw CS Data N95.xlsx"
n95_report_dest = r"C:\Users\jt883\Desktop\CS N95 Report {}.xlsx".format(yesterday)
daily_totals = r"C:\Users\jt883\Desktop\N95 Daily Totals.xlsx"

# Home File Path
# n95_report_path = r"C:\Users\ejin3\OneDrive\Desktop\N95 Report.xlsx"
# unit_total_path = r"C:\Users\ejin3\OneDrive\Desktop\Raw CS Data N95.xlsx"
# n95_report_dest = r"C:\Users\ejin3\OneDrive\Desktop\CS N95 Report {}.xlsx".format(yesterday)
# daily_totals = r"C:\Users\ejin3\OneDrive\Desktop\N95 Daily Totals.xlsx"

sheet_1 = rename_n95_report(n95_report_path)

unit_totals(unit_total_path, n95_report_dest)
format_report(n95_report_dest)
add_daily_total(daily_totals, n95_report_dest, unit_total_path)
