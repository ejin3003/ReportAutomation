import pandas as pd
import psycopg2
import sys
from sql.sql_upload import connect, single_insert


def main():
    param_dic = {
        "host":  "localhost",
        "database": "epic_data",
        "user": "postgres",
        "password": "Dragonleaf7"
    }

    mm_staff = r"C:\Users\tyson\OneDrive\Desktop\MM Staff.xlsx"
    df = pd.read_excel(mm_staff)

    for i in df.index:
        id = df['id'][i]
        badge_id = df['badge_id'][i]
        username = df['username'][i]
        last_name = df['last_name'][i]
        first_name = df['first_name'][i]
        gender = df['gender'][i]
        pay_status = df['pay_status'][i]
        dept_id = df['dept_id'][i]
        dept_name = df['dept_name'][i]
        work_group = df['work_group'][i]
        job_code = df['job_code'][i]
        job_title = df['job_title'][i]
        shift = df['shift'][i]
        reg_temp = df['reg_temp'][i]
        standard_hrs = df['standard_hrs'][i]
        fte = df['fte'][i]
        email = df['email'][i]
        location = df['location'][i]
        columns = "id, badge_id, username, last_name, first_name, gender, pay_status, dept_id, dept_name," \
                  " work_group, job_code, job_title, shift, reg_temp, standard_hrs, fte, email, location"
        values = (id, badge_id, username, last_name, first_name, gender, pay_status, dept_id, dept_name,
                  work_group, job_code, job_title, shift, reg_temp, standard_hrs, fte, email, location)

        # query = "INSERT INTO table_name(col_1, col_1) VALUES(%, '%');" % (val_1, val_2)
        query = f"INSERT INTO mm_staff({columns}) VALUES(%s, %s, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', %s, '%s', '%s', '%s', '%s', %s, '%s', '%s');" % values

        conn = connect(param_dic)
        single_insert(conn, query)
        conn.close()


main()
