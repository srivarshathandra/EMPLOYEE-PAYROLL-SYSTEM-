import mysql.connector


db_connect = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Srivarsha@1234",
    database="employee_payroll_system"
)

print("Connected successfully!")


cursor = db_connect.cursor()
