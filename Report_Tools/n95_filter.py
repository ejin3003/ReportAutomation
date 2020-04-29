import pandas as pd

report = pd.read_excel(r"C:\Users\ejin3\OneDrive\Desktop\Raw CS Data N95.xlsx")
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', None)
report.columns = ['Mask', 'Date', 'Unit', 'Qty']
report['Mask'] = report['Mask'].astype('category')
report['Date'] = report['Date'].dt.date

report['Mask'].replace({
    'FILTER PFR95 RESPIRATOR REG SIZE': 'Halyard Duckbill Reg',
    'GERSON N95 MASK RESPIRATOR 1730': 'Gerson 1730',
    'GERSON N95 MASK RESPIRATOR 82130': 'Gerson 82130',
    'MASK FACE RESPIRATOR N95 SMALL BX/20EA': '3M 1860S Small',
    'MASK RESPIRATOR PARTICULATE CONE N95 NIOSH CERTIFIED FLUID R': '3M 1860 Regular',
    'MASK RESPIRATOR SM CS/6BX/35EA': 'Halyard Duckbill Small'
}, inplace=True)

# Multi Index Version
report = report[['Unit', 'Date', 'Mask', 'Qty']]
multi_index_df = report.set_index(keys=['Unit']).sort_values(['Unit', 'Date'])
print(multi_index_df)
multi_index_df.to_excel(r"C:\Users\ejin3\OneDrive\Desktop\CS Data N95 4.27.xlsx")

# Hold
# multi_index_df = n95.set_index(keys=['Date', 'Unit']).sort_values('Unit')

# Totals >> Requires Fix
# mgh_units = n95.groupby(['Unit', 'Date', 'Mask'])['Qty'].sum().unstack(level=['Date', 'Mask'])
# mgh_units = mgh_units.assign(total=mgh_units.sum(1))
# mgh_units = mgh_units.stack(level='Date')
# mgh_units = mgh_units.assign(total=mgh_units.sum(1))
# mgh_units = mgh_units.stack(level='Mask')
# print(mgh_units)
# mgh_units.to_excel(r"C:\Users\jt883\Desktop\N95 Version 3.xlsx")


# Basic Groupby Version
# mgh_units = n95.groupby(['Unit', 'Date', 'Mask'])
# mgh_units.sum().to_excel(r"C:\Users\jt883\Desktop\N95 Version 2.xlsx")




