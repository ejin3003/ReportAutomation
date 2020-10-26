import pandas as pd
"""
MS SERVER FOLDER: DAILY_CART_COUNT
"""

path = r"C:\Users\ejin3\OneDrive\Desktop\Materials Service\MS Server Dump\DAILY_CART_COUNT\JB_PHSIN159_SCHEDULE-26880938.csv"

df = pd.read_csv(path, encoding='unicode_escape')

print(df.head())
