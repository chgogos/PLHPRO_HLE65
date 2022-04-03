import sqlite3
from sqlite3 import Error

def dbconnect(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

my_conn = dbconnect ('users_database.db')

sql_query = "CREATE TABLE users (id INTEGER PRIMARY KEY, username VARCHAR(128), password VARCHAR(128), name TEXT);"
c = my_conn.cursor()
c.execute(sql_query)

my_conn.close()