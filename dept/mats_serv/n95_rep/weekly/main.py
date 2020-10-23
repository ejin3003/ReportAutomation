from dept.mats_serv.n95_rep.weekly.rep_tools.rename_report_cells import rename_n95_report
from dept.mats_serv.n95_rep.weekly.rep_tools.unit_totals import unit_totals
from dept.mats_serv.n95_rep.weekly.rep_tools.append_to_df import add_daily_total
from dept.mats_serv.n95_rep.weekly.rep_tools.rep_xlsxwriter import create_raw_report, create_n95_report, create_daily_totals_ref
from datetime import date
from datetime import timedelta

prev_week = str(date.today() - timedelta(days=7)) + "..." + str(date.today())


def main():
    """
    Weekly N95 Report: Produces an excel report which displays the quantity of "N95 Masks" ordered by unit for the past
    7 days.
    """
    # File Paths & Destinations
    n95_rep_path = r"C:\Users\jt883\Desktop\N95 Report.xlsx"
    raw_csdata_path = r"C:\Users\ejin3\OneDrive\Desktop\Raw CS Data N95.xlsx"
    weekly_totals_path = r"C:\Users\ejin3\OneDrive\Desktop\N95 Weekly Totals.xlsx"
    dest_n95_rep = r"C:\Users\ejin3\OneDrive\Desktop\CS N95 Report {}.xlsx".format(prev_week)

    # Creates DataFrames for the construction of the "Weekly N95 Report"


if __name__ == "__main__":
    main()

