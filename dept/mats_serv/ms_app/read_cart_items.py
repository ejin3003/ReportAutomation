import pandas as pd
path = r"C:\Users\tyson\OneDrive\Desktop\MS\JB_CART_ITEMS_ALL_PHS_CARTS\JB_CART_ITEMS_MGH-26812916.csv"
# path.encode('utf-8').strip()
df_1 = pd.read_csv(path, encoding='unicode_escape')

print(df_1.head())
