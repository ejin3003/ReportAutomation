import pandas as pd

report = pd.read_excel(r"C:\Users\ejin3\OneDrive\Desktop\CS Data N95 4.27.xlsx")
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', None)
report['Mask'] = report['Mask'].astype('category')
report['Date'] = report['Date'].dt.date
unit_total = report[['Unit', 'Qty']]
unit_total.columns = ['Unit', 'Unit Total']

# Unit Totals
units = unit_total.groupby('Unit')
df = pd.DataFrame(units.sum()).sort_values('Unit Total', ascending=False)
df.to_excel(r"C:\Users\ejin3\OneDrive\Desktop\Unit Total 4.27.xlsx")






