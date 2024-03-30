import mysql.connector

# Database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ab@6367802080",
    database="gym_management_system"
)

if conn.is_connected():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM STAFF")

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    conn.close()
else:
    print("Failed to connect to the database")
