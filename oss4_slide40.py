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

sql_query = "DELETE FROM users WHERE id='3';"
c = my_conn.cursor()
res = c.execute(sql_query)

my_conn.commit()

my_conn.close()