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

sql_query = "SELECT * FROM users;"
c = my_conn.cursor()
result = c.execute(sql_query)
for rec in result.fetchall():
  print(rec)

my_conn.close()