import mysql.connector

# Database connection
# for mysql use name run query( SELECT USER(); )
# -- This query will return a result like 'username'@'hostname'.
conn = mysql.connector.connect(
    host="localhost",
    user="your_my_sql_server_ussername",
    password="your_my_sql_server_password",
    database="gym_management_system"
)


if conn.is_connected():
    print("Connected to the database")
else:
    print("Failed to connect to the database")
