import psycopg2
import pandas as pd

data = pd.DataFrame({
    "num": [22, 33, 44],
    "data": ["test1", "test2", "test3"]
})
conn = psycopg2.connect('dbname=postgres user=postgres password=Dragonleaf7')
cur = conn.cursor()






# Connect to PostgreSql Database
# conn = psycopg2.connect('dbname=postgres user=postgres password=Dragonleaf7')
#
# cur = conn.cursor()
# cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
# cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abc'def"))
# cur.execute("SELECT * FROM test;")
#
# test = cur.fetchone()
# print(test)
# conn.commit()
# cur.close()
# conn.close()
