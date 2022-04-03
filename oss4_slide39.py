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

sql_query = "SELECT username FROM users;"
c = my_conn.cursor()
records = c.execute(sql_query)
for rec in records.fetchall():
  print(rec)
my_conn.close()

my_conn = dbconnect ('users_database.db')

sql_query = "SELECT name FROM users WHERE id=2;"
c = my_conn.cursor()
records = c.execute(sql_query)
for rec in records.fetchall():
  print(rec)
my_conn.close()