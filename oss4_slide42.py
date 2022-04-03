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

sql_query = "PRAGMA table_info('Users')"
c = my_conn.cursor()
res = c.execute(sql_query)
for item in res.fetchall():
  print(item)

my_conn.close()