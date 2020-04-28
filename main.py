# Renames columns and mask names within the Customer Service N95 Report
from Report_Tools.rename_report_cells import *
n95_report_path = r"C:\Users\ejin3\OneDrive\Desktop\N95 Report 4.27.xlsx"
n95_report_dest = r"C:\Users\ejin3\OneDrive\Desktop\New N95 Report 4.27.xlsx"
rename_n95_report(n95_report_path, n95_report_dest)

# Appends units totals to n95_report_dest
