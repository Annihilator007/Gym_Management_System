import mysql.connector

# Database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ab@6367802080",
    database="gym_management_system"
)

if conn.is_connected():
    print("Connected to the database")
else:
    print("Failed to connect to the database")
