import pandas as pd
from openpyxl import load_workbook


def unit_totals(path):
    unit_report = pd.read_excel(path)
    pd.set_option('display.width', 400)
    pd.set_option('display.max_columns', None)
    unit_report.columns = ['Mask', 'Date', 'Unit', 'Qty']
    unit_report = unit_report[['Unit', 'Date', 'Mask', 'Qty']]
    unit_report['Mask'] = unit_report['Mask'].astype('category')
    unit_report['Date'] = unit_report['Date'].dt.date

    unit_report['Mask'].replace({
        'FILTER PFR95 RESPIRATOR REG SIZE': 'Halyard Duckbill Reg',
        'GERSON N95 MASK RESPIRATOR 1730': 'Gerson 1730',
        'GERSON N95 MASK RESPIRATOR 82130': 'Gerson 82130',
        'MASK FACE RESPIRATOR N95 SMALL BX/20EA': '3M 1860S Small',
        'MASK RESPIRATOR PARTICULATE CONE N95 NIOSH CERTIFIED FLUID R': '3M 1860 Regular',
        'MASK RESPIRATOR SM CS/6BX/35EA': 'Halyard Duckbill Small'
    }, inplace=True)

    unit_report = unit_report.set_index("Date")

    # Unit Totals DataFrame
    unit_total = unit_report[['Unit', 'Qty']]
    unit_total.columns = ['Unit', 'Unit Total']
    units = unit_total.groupby('Unit')
    unit_total = pd.DataFrame(units.sum()).sort_values('Unit Total', ascending=False)

    return unit_report, unit_total
