import pandas as pd
from rep_tools.alter.act_rep_cleaner import clean_act_rep
from dept.rep_func_new.extract_data import ExtractData

act_rep_path = r"C:\Users\tyson\OneDrive\Desktop\MGH\EPIC\ACT. REPS\Oct 2020 Act Rep.xlsx"
prod_rep_path = r"C:\Users\tyson\OneDrive\Desktop\MGH\EPIC\PROD. REPS\Oct 2020 Prod Rep.xlsx"


# act_rep_path = r"C:\Users\jt883\Desktop\July 2020 Act Rep.xlsx"
# prod_rep_path = r"C:\Users\jt883\Desktop\July 2020 Prod Rep.xlsx"

act_df = clean_act_rep(act_rep_path)
prod_obj = ExtractData(prod_rep_path)
prod_df = prod_obj.extract_prod()

act_escort_list = set(act_df["Assigned To"].to_list())
prod_escort_list = prod_df.index

# test_list_1 = [1, 2, 3, 4, 5, 6]
# test_list_2 = [5, 6, 7, 8, 9, 10]
missing_list = []

for escort in act_escort_list:
    if escort not in prod_escort_list:
        missing_list.append(escort)

print(missing_list)
print(len(missing_list))

dest = r"C:\Users\tyson\OneDrive\Desktop\Missing Escorts.xlsx"
# dest = r"C:\Users\jt883\Desktop\Missing Escorts.xlsx"
df = pd.DataFrame(missing_list, columns=["Escorts"])
df.to_excel(dest)

# print(list(prod_df.index))
# print(act_df["Assigned To"].to_list())
