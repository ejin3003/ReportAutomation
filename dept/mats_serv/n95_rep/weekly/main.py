from dept.rep_func_new import alter_cs_n95_rep
from dept.rep_func_new import unit_totals
from dept.rep_func_new import add_weekly_total
from dept.rep_func_new import create_n95_report, create_daily_totals_ref
from datetime import date
from datetime import timedelta
import calendar


def main():
    """
    Weekly N95 Report: Produces an excel report which displays the quantity of "N95 Masks" ordered by unit for the
    past 7 days.
    """
    today_date = date.today()
    day_name = calendar.day_name[today_date.weekday()]
    if day_name == "Monday":

        prev_week = str(date.today() - timedelta(days=7)) + "..." + str(date.today() - timedelta(days=1))

        # File Paths & Destinations
        n95_rep_path = r"C:\Users\jt883\Desktop\N95 Report.xlsx"
        raw_cs_data_path = r"C:\Users\jt883\Desktop\Raw CS Data N95.xlsx"
        weekly_totals_path = r"C:\Users\jt883\Desktop\Weekly N95 Totals.xlsx"
        dest_weekly_n95_rep = r"C:\Users\jt883\Desktop\Weekly CS N95 Report {}.xlsx".format(prev_week)

        # Creates DataFrames for the construction of the "Weekly N95 Report"
        n95_rep_df = alter_cs_n95_rep(n95_rep_path)
        unit_report_df, unit_totals_df, total = unit_totals(raw_cs_data_path)
        weekly_totals_df = add_weekly_total(weekly_totals_path, total)

        # Creates "Weekly N95 Report"
        create_n95_report(dest_weekly_n95_rep, n95_rep_df, unit_totals_df, weekly_totals_df, unit_report_df)
        create_daily_totals_ref(weekly_totals_path, weekly_totals_df)


if __name__ == "__main__":
    main()

# my_date = date.today()
# day_name = calendar.day_name[my_date.weekday()]
# print(day_name)
# print(type(day_name))
