import pandas as pd
"""
MS SERVER FOLDER: DAILY_CART_COUNT
"""
# path = r"C:\Users\ejin3\OneDrive\Desktop\Materials Service\MS Server Dump\DAILY_CART_COUNT\JB_PHSIN159_SCHEDULE-26880938.csv"
path = r"C:\Users\tyson\OneDrive\Desktop\MS\DAILY_CART_COUNT\JB_PHSIN159_SCHEDULE-26880938.csv"
df = pd.read_csv(path, encoding='unicode_escape')

# DataFrame of Locations and Par Location ID
unit_test = df.drop_duplicates(subset=["Location", "Cart ID"])
unit_test = unit_test[["Cart ID", "Location"]].sort_values("Cart ID")
print(unit_test.count())
print(df.head())

