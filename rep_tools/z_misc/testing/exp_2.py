import pandas as pd
from dept.rep_func_new.alter_df import AlterDataframe, JoinTwoDataframes
import xlrd, xlsxwriter

statroom_file = r"C:\Users\jt883\Desktop\statroom.csv"
unit_carts_file = r"C:\Users\jt883\Desktop\unit_carts.csv"

df_1 = pd.read_csv(statroom_file)
df_2 = pd.read_csv(unit_carts_file)

# Create a new dataframe containing unique values from the "Descript" & "Item ID" columns with df_1
# obj_1 = AlterDataframe(df_1)
# unique_item_ps_df = obj_1.build_unique_df(['Descript', 'Item ID'])
# print(unique_item_ps_df.shape)


# Join "unique_item_ps_df" and df_2
# obj_2 = JoinTwoDataframes([df_2, 'Long Descr'], [unique_item_ps_df, 'Descript'])
# joined_df = obj_2.join_df()
#
# print(joined_df['Location'].isnull)

# dest_file = r"C:\Users\jt883\Desktop\test.csv"
# joined_df.to_csv(dest_file)

obj_1 = AlterDataframe(df_2)
unique_item_ps_df = obj_1.build_unique_df(['Item', 'Long Descr'])
print(unique_item_ps_df.shape)

dest_file = r"C:\Users\jt883\Desktop\test_1.xlsx"
unique_item_ps_df.to_excel(dest_file)

