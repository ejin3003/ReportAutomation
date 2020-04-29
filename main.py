from Report_Tools.rename_report_cells import *
from Report_Tools.unit_totals import *

# Renames columns and mask names within the Customer Service N95 Report
n95_report_path = r"C:\Users\jt883\Desktop\N95 Report.xlsx"
n95_report_dest = r"C:\Users\jt883\Desktop\CS N95 Report 4.28.xlsx"
rename_n95_report(n95_report_path, n95_report_dest)

# Appends units totals to n95_report_dest
unit_total_path = r"C:\Users\jt883\Desktop\Raw CS Data N95.xlsx"
unit_total_dest = r"C:\Users\jt883\Desktop\Unit Totals 4.28.xlsx"
unit_totals(unit_total_path, unit_total_dest)
