import sqlite3

my_conn = sqlite3.connect("users_database.db")
sql_query = "SELECT name FROM users WHERE id=1;"
c = my_conn.cursor()
records = c.execute(sql_query)
for rec in records.fetchall():
    print(rec)
my_conn.close()
