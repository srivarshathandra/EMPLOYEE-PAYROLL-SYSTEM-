from db_connection import cursor, db_connect


class Attendance:

    def mark_attendance(self):
        emp_id = int(input("Employee ID: "))
        days = int(input("Days Present: "))

        query = """
        insert into attendance(emp_id, days_present)
        values (%s,%s)
        on duplicate key update days_present=%s
        """

        cursor.execute(query, (emp_id, days, days))
        db_connect.commit()

        print("Attendance Updated")