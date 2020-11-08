import pandas as pd
import os


def column_select():
    """
    Select columns using a letter designation for columns
    """
    cs_df = pd.read_excel(src_file, header=1, usecols='B:F')
    return cs_df


def column_check(x):
    """
    Uses a callable function to exclude/select designated columns
    """
    if 'unnamed' in x.lower():
        return False
    if 'priority' in x.lower():
        return False
    if 'order' in x.lower():
        return True
    return True


# Looks for file in desktop file path
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), r'OneDrive\Desktop')
src_file = r"{}".format(desktop) + r"\shipping_tables.xlsx"

# Uses the column_check function to select columns
df = pd.read_excel(src_file, header=1, usecols=column_check)
print(df)

