class Employee:

    def __init__(self):
        from db_connection import cursor, db_connect
        self.cursor = cursor
        self.db_connect = db_connect

    def add_employee(self):
        name = input("Enter employee name: ")
        dept = input("Enter department: ")

        query = "INSERT INTO employees (name, department) VALUES (%s, %s)"
        self.cursor.execute(query, (name, dept))
        self.db_connect.commit()

        print("Employee added successfully!")

    def view_employees(self):
        self.cursor.execute("SELECT * FROM employees")
        data = self.cursor.fetchall()

        if data:
            print("\n--- Employee List ---")
            for row in data:
                print(row)
        else:
            print("No employees found!")

    def delete_employee(self):
        emp_id = int(input("Enter employee ID: "))

        self.cursor.execute("DELETE FROM employees WHERE emp_id=%s", (emp_id,))
        self.db_connect.commit()

        print("Employee deleted successfully!")
