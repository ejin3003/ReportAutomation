import pandas as pd


def alter_cs_n95_rep(path):
    """
    Function: Alters Customer Service N95 Excel Data
        1. Renames columns
        2. Renames N95 Masks for clarity
    """
    n95_report = pd.read_excel(path)
    pd.set_option('display.width', 400)
    pd.set_option('display.max_columns', None)
    n95_report.columns = ['Unit', 'Date', 'Mask', 'Total', 'Unit Total', 'Grand Total']
    n95_report['Mask'] = n95_report['Mask'].astype('category')
    # n95_report['Date'] = n95_report['Date'].dt.date
    n95_report.set_index('Date', inplace=True)

    n95_report['Mask'].replace({
        'FILTER PFR95 RESPIRATOR REG SIZE': 'Halyard Duckbill Reg',
        'GERSON N95 MASK RESPIRATOR 1730': 'Gerson 1730',
        'GERSON N95 MASK RESPIRATOR 82130': 'Gerson 82130',
        'MASK FACE RESPIRATOR N95 SMALL BX/20EA': '3M 1860S Small',
        'MASK RESPIRATOR PARTICULATE CONE N95 NIOSH CERTIFIED FLUID R': '3M 1860 Regular',
        'MASK RESPIRATOR SM CS/6BX/35EA': 'Halyard Duckbill Small'
    }, inplace=True)

    return n95_report


# Runs Function Independently
# n95_report_path = r"C:\Users\jt883\Desktop\N95 Report.xlsx"
# dest = r"C:\Users\jt883\Desktop\N95 Rep 10.12.20...10.18.20.xlsx"
# n95_rep = rename_n95_report(n95_report_path)
# n95_rep.to_excel(dest)
