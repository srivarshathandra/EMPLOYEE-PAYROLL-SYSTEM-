from db_connection import cursor, db_connect


class Employee:

    def __init__(self):
        self.cursor = cursor
        self.db_connect = db_connect


    # REGISTER
    def register(self):
        name = input("Enter name: ")
        dept = input("Enter department: ")
        username = input("Enter username: ")
        password = input("Enter password: ")
        confirm = input("Confirm password: ")

        if password != confirm:
            print("Passwords do not match!")
            return

        try:
            query = """
            INSERT INTO employees (name, department, username, password)
            VALUES (%s, %s, %s, %s)
            """
            self.cursor.execute(query, (name, dept, username, password))
            self.db_connect.commit()

            print("Registration Successful")

        except Exception as e:
            print("Error:", e)


    # LOGIN
    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")

        query = """
        SELECT emp_id, name
        FROM employees
        WHERE username=%s AND password=%s
        """

        self.cursor.execute(query, (username, password))
        user = self.cursor.fetchone()

        if user:
            print(f"Welcome {user[1]}")
            return user[0]
        else:
            print("Invalid Credentials")
            return None


    # ADD EMPLOYEE
    def add_employee(self):
        name = input("Enter employee name: ")
        dept = input("Enter department: ")

        query = "insert into employees (name, department) VALUES (%s, %s)"
        self.cursor.execute(query, (name, dept))
        self.db_connect.commit()

        print("Employee added successfully!")


    # VIEW EMPLOYEES
    def view_employees(self):
        self.cursor.execute("select emp_id, name, department from employees")
        data = self.cursor.fetchall()

        print("\n--- EMPLOYEE LIST ---")
        for row in data:
            print(f"ID: {row[0]} | Name: {row[1]} | Dept: {row[2]}")


    # DELETE EMPLOYEE
    def delete_employee(self):
        emp_id = int(input("Enter employee ID: "))

        self.cursor.execute("delete from employees where emp_id=%s", (emp_id,))
        self.db_connect.commit()

        print("Employee deleted successfully!")