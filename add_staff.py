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

    name = input("Enter name: ")
    mobile = input("Enter mobile number: ")
    salary = int(input("Enter salary: "))

    cursor.execute("INSERT INTO STAFF (NAMES, MOB_NO, SALARY) VALUES (%s, %s, %s)", (name, mobile, salary))
    conn.commit()

    print("New staff member added successfully")

    cursor.close()
    conn.close()
else:
    print("Failed to connect to the database")
