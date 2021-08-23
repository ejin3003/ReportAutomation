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

    def single_insert(self, columns_dict):
        """Inserts data into sequel database one row at a time"""
        pass


class SequelQuery:

    def __init__(self):
        self.dct = {}

    def build_upload_query(self, **kwargs):
        """{"column_name": "str or int"}"""
        pass


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
