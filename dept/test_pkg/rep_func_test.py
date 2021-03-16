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


# def test_build_unique_df():
#     cols = ["Assigned To", "Epic ID"]
#     data = [["Erza", 101], ["Sepra", 102], ["Erza", 101], ["Ejin", 103], ["Sepra", 102]]
#     df = pd.DataFrame(data, columns=cols)


