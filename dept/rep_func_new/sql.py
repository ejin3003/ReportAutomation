import sys
import psycopg2


class PostgreSQL:
    def __init__(self):
        self.dct = {}

    def connect(self, **kwargs):
        """Connects to the designated database"""
        self.dct = kwargs
        try:
            # Connect to database server
            print(kwargs)
            print("Connected to database")
            conn = psycopg2.connect(**kwargs)
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
            sys.exit(1)
        return conn

    def single_insert(self, sql_query):
        """Inserts data into sequel database one row at a time"""
        pass


class SequelQuery:

    def __init__(self, df):
        self.df = df

    def build_query_list(self, columns_dct):
        """{"column_name": "str or int"}"""
        col_name_str = ' ,'.join(columns_dct.keys())
        positionals = ','.join(columns_dct.values())
        positionals = positionals.replace("str", "'%s'").replace("int", "%s")
        base_query = f"INSERT INTO prod_data({col_name_str}) VALUES({positionals})"
        gen_obj = ((tuple(self.df.iloc[row_num]) for row_num in range(len(self.df.index))))
        values_list = list(gen_obj)
        sql_list = []
        for _, values in enumerate(values_list):
            sql_list.append(base_query % values)
        return sql_list


param_dict = {
    "host": "localhost",
    "database": "epic_data",
    "user": "postgres",
    "password": "mgh3003"
}


# Test 1: Connection
# If you want to pass the dictionary contents as keyword arguments you need to unpack it (** in front of the dict).
# conn = PostgreSQL().connect(**param_dict)
# conn.close()
