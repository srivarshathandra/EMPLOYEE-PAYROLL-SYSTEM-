from db_connection import cursor, db_connect


class Salary:

    def update_salary(self):
        emp_id = int(input("Employee ID: "))
        base = float(input("Base Salary: "))
        bonus = float(input("Bonus: "))

        query = """
        insert into salary(emp_id, base_salary, bonus)
        values (%s,%s,%s)
        on duplicate key UPDATE base_salary=%s, bonus=%s
        """

        cursor.execute(query, (emp_id, base, bonus, base, bonus))
        db_connect.commit()

        print("Salary Updated")