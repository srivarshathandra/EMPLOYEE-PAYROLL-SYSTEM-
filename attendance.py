class Attendance:

    def __init__(self):
        from db_connection import cursor, db_connect
        self.cursor = cursor
        self.db_connect = db_connect

    def mark_attendance(self):
        emp_id = int(input("Enter employee ID: "))
        days = int(input("Enter days present: "))

        query = """
        replace into attendance (emp_id, days_present)
        values (%s, %s)
        """

        self.cursor.execute(query, (emp_id, days))
        self.db_connect.commit()

        print("Attendance updated successfully!")
        
        