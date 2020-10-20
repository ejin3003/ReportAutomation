import pandas as pd
# Read comma separated text file

df = pd.read_csv(r"C:\Users\jt883\Desktop\employeebadgenumbers.txt", sep=":", error_bad_lines=False, encoding="latin1")
df.columns = ["AB"]

df = df["AB"].str.split(",", 2, expand=True)
df.columns = ["Badge ID", "Full Name", "Employee ID"]
pd.DataFrame(data=df)
df["Badge ID"] = df["Badge ID"]

# df.set_index("Badge ID", inplace=True)

# df.to_excel(r"C:\Users\jt883\Desktop\employeebadgenumbers.xlsx")

print(df.info())

# mask = df["Badge ID"] == 173605
# print(df[mask])
