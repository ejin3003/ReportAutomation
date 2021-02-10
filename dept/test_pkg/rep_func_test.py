import pandas as pd
from dept.rep_func_new.extract_data import ExtractData


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


# test_extract_prod()
# Target Type: <class 'pandas.core.frame.DataFrame'>
