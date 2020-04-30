import pandas as pd
from openpyxl import load_workbook


def unit_totals(path, dest):
    report = pd.read_excel(path)
    pd.set_option('display.width', 400)
    pd.set_option('display.max_columns', None)
    report.columns = ['Mask', 'Date', 'Unit', 'Qty']
    report = report[['Unit', 'Date', 'Mask', 'Qty']]
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

    # Unit Totals
    unit_total = report[['Unit', 'Qty']]
    unit_total.columns = ['Unit', 'Unit Total']
    units = unit_total.groupby('Unit')
    df = pd.DataFrame(units.sum()).sort_values('Unit Total', ascending=False)

    # Add Units Totals Sheet to N95 Report
    writer = pd.ExcelWriter(dest, engine="openpyxl")
    book = load_workbook(dest)
    writer.book = book
    df.to_excel(writer, sheet_name="Unit Totals")
    sheet = book.get_sheet_by_name("Unit Totals")
    sheet.column_dimensions["A"].width = 30
    writer.save()
    writer.close()
