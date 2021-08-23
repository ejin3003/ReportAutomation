import pandas as pd
from dept.rep_func_new.sql import SequelQuery


column_names = ['first_name', 'last_name', 'ID', 'shift', 'Total']
data = [['Erza', 'Scarlet', 1, 'Day', 77], ['Ejin', 'Moonlight', 2, 'Day', 24], ['Vawn', 'Fair', 3, 'Day', 33]]
df = pd.DataFrame(data, columns=column_names)
columns_dct = {'first_name': 'str', 'last_name': 'str', 'ID': 'int', 'shift': 'str', 'Total': 'int'}
col_name_str = ' ,'.join(columns_dct.keys())
positionals = ','.join(columns_dct.values())
positionals = positionals.replace("str", "'%s'").replace("int", "%s")
row1_values = df.iloc[0]
sql_query = f"INSERT INTO prod_data({col_name_str}) VALUES({positionals})"
print(tuple(row1_values))

tup_comp = (x for x in df)