import pandas as pd
import numpy as np
from dept.rep_func_new.extract_data import ExtractData
from dept.rep_func_new.alter_df import AlterDataframe


def test_extract_prod():
    """Output should be a pandas dataframe."""
    cols = ["Transporter", "Guild", "Gender"]
    data = [
        ["Erza", "Fairy Tale", "F"],
        ["Ejin", "Moonlight Knights", "M"],
        ["Sepra", "Solo", "F"],
        ["Average", "MGH", "M"]
    ]
    df = pd.DataFrame(data, columns=cols)
    obj = ExtractData(df)
    new_df = obj.extract_prod()
    assert str(type(new_df)) == "<class 'pandas.core.frame.DataFrame'>"


def test_fill_null_set_type():
    """Tests the output of the function"""
    cols = ["Fruit", "Quantity"]
    data = [["Apple", np.nan], [np.nan, np.nan], ["Pear", 3]]
    # dct = {"column_1": ["Fruit", "str"], "column_2": ["Quantity", "int"]}
    dct = {"Fruit": "str", "Quantity": "int"}
    df = pd.DataFrame(data, columns=cols)
    obj_df = AlterDataframe(df)
    df = obj_df.fill_null_set_type(dct)
    df_lst = df.values.tolist()
    assert df_lst == [['Apple', 0], ['Unknown', 0], ['Pear', 3]]


def test_filter_out_rows():
    cols = ["Name", "Position", "Status"]
    data = [["Erza", "Leader", "Active"], ["Atlas", "Knight", "In-Active"], ["Sepra", "Spy", "Active"]]
    df = pd.DataFrame(data, columns=cols)
    dct = {"Position": ["Spy"], "Status": ["In-Active"]}
    obj_df = AlterDataframe(df)
    df = obj_df.filter_out_rows(dct)
    df_lst = df.values.tolist()
    assert df_lst == [["Erza", "Leader", "Active"]]


def test_build_unique_df():
    cols = ["Name", "Position", "epic_id"]
    data = [["Erza", "Leader", 101], ["Atlas", "Knight", 102], ["Sepra", "Spy", 103], ["Erza", "Leader", 101]]
    test_df = pd.DataFrame(data, columns=cols)
    dct = ["Name", "epic_id"]
    obj_df = AlterDataframe(test_df)
    df = obj_df.build_unique_df(dct)
    df_lst = df.values.tolist()    # Removes array from the last column
    assert df_lst == [['Atlas', 102], ['Erza', 101], ['Sepra', 103]]


def test_join_dataframes():
    cols_1, cols_2 = ["Name", "ID"], ["ID", "Shift"]
    data_1, data_2 = [["Erza", 1], ["Ejin", 3], ["Sepra", 2]], [[2, "Evening"], [3, "Day"], [1, "Night"]]
    df_1, df_2 = pd.DataFrame(data_1, columns=cols_1), pd.DataFrame(data_2, columns=cols_2)
    join_lst = ["ID", "ID"]
    joined_df = AlterDataframe(df_1).join_dataframes(df_2, join_lst)
    lst_df = joined_df.values.tolist()
    assert lst_df == [["Erza", "Night"], ["Ejin", "Day"], ["Sepra", "Evening"]]

