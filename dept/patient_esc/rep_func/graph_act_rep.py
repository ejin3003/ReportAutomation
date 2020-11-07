from clean.act_rep_cleaner import *
from graph.graph_config import *
from graph.seaborn_graph import *
from graph.df_for_plt import *
from graph.df_for_sns import *
from decorators.measure_performace import timer


@timer
def testing_graph():
    # Cleans and filters Epics Activity Report
    path = r"C:\Users\tyson\OneDrive\Desktop\Aug 2020 Act Rep.xlsx"
    df = clean_act_rep(path)

    """ 
    The custom functions below create graphs using MatPlotLib & SeaBorn
    """

    # DataFrame & Graph >> Comprehensive daily total of central trips >> MatPlotLib
    df_daily_totals = DataFramePltGraph(df, "Transport Date", ["Date", "Daily Total"])
    df_daily_totals = df_daily_totals.create_totals_df()
    graph_daily_trip_totals(df_daily_totals)

    # DataFrame & Graph >> Individual totals of central trips
    df_escort_totals = DataFrameSnsGraph(df, "Assigned To", False, ["Escort Total"], None)
    df_escort_totals = df_escort_totals.create_size_sns_df()
    sns_graph_1 = SnsGraph(df_escort_totals, "Central: Total Trips Completed", (14, 20), "plasma")
    sns_graph_1.sns_bar_plot()

    # DataFrame & Graph >> Individual daily average of completed trips
    df_escort_avg = DataFrameSnsGraph(df, "Assigned To", True, ["Escort Averages"], "Asgn->Cmp")
    df_escort_avg = df_escort_avg.create_mean_sns_df()
    sns_graph_2 = SnsGraph(df_escort_avg, "Central: Escort Average Time To Complete", (14, 20), "summer")
    sns_graph_2.sns_bar_plot()

    # DataFrame & Graph >> Individual daily average time to acknowledge
    df_escort_ack = DataFrameSnsGraph(df, "Assigned To", False, ["Average Time to Acknowledge"], "Asgn->Ack")
    df_escort_ack = df_escort_ack.create_mean_sns_df()
    sns_graph_3 = SnsGraph(df_escort_ack, "Central: Average Time to Acknowledge", (14, 20), "Blues_d")
    sns_graph_3.sns_bar_plot()


testing_graph()
