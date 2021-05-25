import pandas as pd
import psycopg2
from psycopg2.extensions import AsIs
import sys


def connect(params_dic):
    """ Connect to the PostgreSQL database server"""
    conn = None
    try:
        # Connect to PostgreSQL Server
        print('Connects to PostgreSQL database')
        conn = psycopg2.connect(**params_dic)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1)

    return conn


def single_insert(conn, insert_req):
    """ Execute a single INSERT Request """
    cursor = conn.cursor()
    try:
        cursor.execute(''.join(insert_req))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    cursor.close()


def main(path):
    param_dic = {
        "host":  "localhost",
        "database": "epic_data",
        "user": "postgres",
        "password": "mgh3003"
    }

    prod_rep = path
    df = pd.read_excel(prod_rep)

    for i in df.index:
        fullname = df['Transporter'][i]
        completed = df['Completed'][i]
        canceled = df['Canceled'][i]
        outliers = df['Outliers'][i]
        escalations = df['Escalations'][i]
        delay_time = df['Delay Time'][i]
        ack_inp = df['Ack -> In P'][i]
        inp_cmp = df['In P -> Comp'][i]
        ack_comp = df['Ack -> Comp'][i]
        working_time = df['Working Time'][i]
        idle_time = df['Idle Time'][i]
        break_time = df['Break Time'][i]
        work_days = df['Work Days'][i]
        total_patient = df['Total Patient'][i]
        total_non_patient = df['Total Non-Patient'][i]
        month = df['Month'][i]
        epic_id = df['Assigned To ID'][i]
        columns = "fullname, completed, canceled, outliers, escalations, delay_time, ack_inp, inp_comp, ack_comp," \
                  " working_time, idle_time, break_time, work_days, total_patient, total_non_patient, month, epic_id"
        values = (fullname, completed, canceled, outliers, escalations, delay_time, ack_inp, inp_cmp, ack_comp,
                  working_time, idle_time, break_time, work_days, total_patient, total_non_patient, month, epic_id)

        # query = "INSERT INTO table_name(col_1, col_1) VALUES(%, '%');" % (val_1, val_2)
        query = f"INSERT INTO prod_data({columns}) VALUES('%s', %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, '%s', %s);" % values

        conn = connect(param_dic)
        single_insert(conn, query)
        conn.close()


# rep_path = r"C:\Users\jt883\Desktop\MGH\EPIC\Escort Data\Reps Altered\Prod Extract Jan 2021.xlsx"
# rep_path = r"C:\Users\jt883\Desktop\Prod Extract Apr 2021.xlsx"
# main(rep_path)


# prod_rep = r"C:\Users\tyson\OneDrive\Desktop\July 2020 Prod Rep.xlsx"
# df = pd.read_excel(prod_rep)
# print(df.head(3))

# import uuid
# print(uuid.uuid4())

# df = pd.DataFrame({
#         "num": [22, 33, 44],
#         "data": ["test1", "test2", "test3"]
#     })
#
# columns = [x for x in df.columns]
#
# for i in df.index:
#     num = df['num'][i]
#     data = df['data'][i]
#
#     print(num, data)


# column_1 = 10
# column_2 = 'zzzz'
#
# query = "INSERT INTO test (num, data) VALUES (10, 'zzzz')"
# query_2 = """
# INSERT INTO test(num, data) VALUES(%s, '%s')
# """ %(column_1, column_2)
#
# print(type(query))
# print(query)
# print(type(query_2))
# print(query_2)
