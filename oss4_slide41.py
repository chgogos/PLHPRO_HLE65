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

sql_query = "UPDATE users SET username = 'username_2x', password = 'password_2x' WHERE id='2';"
c = my_conn.cursor()
res = c.execute(sql_query)
my_conn.commit()

my_conn.close()