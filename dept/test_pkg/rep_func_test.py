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
    # Create a "Pandas DataFrame" & "Reference Dictionary" to test the function
    cols = ["Fruit", "Quantity"]
    data = [["Apple", np.nan], [np.nan, np.nan], ["Pear", 3]]
    dct = {"column_1": ["Fruit", "str"], "column_2": ["Quantity", "int"]}
    df = pd.DataFrame(data, columns=cols)
    # Test Function
    obj_df = AlterDataframe(df, dct)
    df = obj_df.fill_null_set_type()
    # print(df)
    df_lst = df.values.tolist()
    assert df_lst == [['Apple', 0], ['Unknown', 0], ['Pear', 3]]


# test_fill_null_set_type()
