class Payslip:

    def __init__(self):
        from db_connection import cursor
        self.cursor = cursor

    def generate_payslip(self):
        emp_id = int(input("Enter employee ID: "))

        query = """
        
        select e.name, e.department, s.base_salary, s.bonus, a.days_present
        from employees e
        join salary s 
        on e.emp_id = s.emp_id
        join attendance a on e.emp_id = a.emp_id
        where e.emp_id = %s
        
        """

        self.cursor.execute(query, (emp_id,))
        data = self.cursor.fetchone()

        if data:
            name, dept, salary, bonus, days = data
            total = salary + bonus

            print("\n----- PAYSLIP -----")
            print("Name:", name)
            print("Department:", dept)
            print("Base Salary:", salary)
            print("Bonus:", bonus)
            print("Days Present:", days)
            print("Total Salary:", total)
        else:
            print("No record found! Make sure salary and attendance are added.")