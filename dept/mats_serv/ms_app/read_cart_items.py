import pandas as pd
"""
MS SERVER FOLDER: JB_CART_ITEMS_ALL_PHS_CARTS
"""

# path = r"C:\Users\tyson\OneDrive\Desktop\MS\JB_CART_ITEMS_ALL_PHS_CARTS\JB_CART_ITEMS_MGH-26812916.csv"
# path = r"C:\Users\ejin3\OneDrive\Desktop\Materials Service\MS Server Dump\JB_CART_ITEMS_ALL_PHS_CARTS\JB_CART_ITEMS_MGH-26812916.csv"
path = r"C:\Users\jt883\Desktop\MS\JB_CART_ITEMS_ALL_PHS_CARTS\JB_CART_ITEMS_MGH-26812916.csv"
# path.encode('utf-8').strip()
df_1 = pd.read_csv(path, encoding='unicode_escape')
loc_id_obj = df_1.groupby("Par Location ID")
# loc_df = loc_id_obj["Location"]

# DataFrame of Locations and Par Location ID
unit_test = df_1.drop_duplicates(subset=["Location", "Par Location ID"])
unit_test = unit_test[["Par Location ID", "Location"]].sort_values("Par Location ID")
print(unit_test.count())

dest = r"C:\Users\jt883\Desktop\units.xlsx"
unit_test.to_excel(dest)

# Sorts DataFrame by specified values
# df_1.sort_values("Par Location ID", inplace=True)

# Create a DataFrame of unique values
# units = df_1.Location.unique()
# unit_df = pd.DataFrame(units)

