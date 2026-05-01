class Payroll:

    def __init__(self):
        from db_connection import cursor, db_connect
        self.cursor = cursor
        self.db_connect = db_connect

    def update_salary(self):
        emp_id = int(input("Enter employee ID: "))
        base_salary = float(input("Enter base salary: "))

        bonus = base_salary * 0.10

        query = """
        replace into salary (emp_id, base_salary, bonus)
        values (%s, %s, %s)
        """

        self.cursor.execute(query, (emp_id, base_salary, bonus))
        self.db_connect.commit()

        print("Salary updated successfully!")
        