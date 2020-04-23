import pandas as pd

# Imports Data and Renames the Columns
report = pd.read_excel(r"C:\Users\jt883\Desktop\N95 Reports\N95 Report 4.23.xlsx")
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', None)
report.columns = ['Mask', 'Date', 'Unit', 'Qty']
report['Mask'] = report['Mask'].astype('category')
report['Date'] = report['Date'].dt.date

# Renames N95 Masks
report['Mask'].replace({
    'FILTER PFR95 RESPIRATOR REG SIZE': 'Halyard Duckbill Reg',
    'GERSON N95 MASK RESPIRATOR 1730': 'Gerson 1730',
    'GERSON N95 MASK RESPIRATOR 82130': 'Gerson 82130',
    'MASK FACE RESPIRATOR N95 SMALL BX/20EA': '3M 1860S Small',
    'MASK RESPIRATOR PARTICULATE CONE N95 NIOSH CERTIFIED FLUID R': '3M 1860 Regular',
    'MASK RESPIRATOR SM CS/6BX/35EA': 'Halyard Duckbill Small'
}, inplace=True)

# Create a Data Frame with the Subtotals of each Unit
df = report[['Unit', 'Qty']]
df.sort_values(['Unit', 'Qty'], ascending=[True, False], inplace=True)
df.set_index(['Unit'], inplace=True)
print(df)

# Multi Index Data Frame >> Repositions the Columns and Outputs an Excel Document
# report = report[['Unit', 'Date', 'Mask', 'Qty']]
# multi_index_df = report.set_index(keys=['Unit']).sort_values(['Unit', 'Date'])
# print(multi_index_df)
# multi_index_df.to_excel(r"C:\Users\jt883\Desktop\N95 Reports Altered\N95 Report.xlsx")





