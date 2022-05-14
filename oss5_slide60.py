import sqlite3

my_conn = sqlite3.connect("users_database.db")
sql_query = (
    "INSERT INTO users (id, username, password) VALUES ('1','user_1', 'password_1');"
)
c = my_conn.cursor()
c.execute(sql_query)

my_conn.commit()
my_conn.close()
