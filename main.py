from employees import Employee
from salary import Salary
from attendance import Attendance
from payslip import Payslip

e = Employee()
s = Salary()
a = Attendance()
p = Payslip()

print("1. Register")
print("2. Login")

choice = int(input("Enter choice: "))

if choice == 1:
    e.register()

elif choice == 2:
    emp_id = e.login()

    if emp_id:
        while True:
            print("\n--- Welcome to Employee Payroll System ---")
            print("1. Add Employee")
            print("2. View Employees")
            print("3. Delete Employee")
            print("4. Update Salary")
            print("5. Mark Attendance")
            print("6. Generate Payslip")
            print("7. Exit")

            choice = int(input("Enter choice: "))

            if choice == 1:
                e.add_employee()
            elif choice == 2:
                e.view_employees()
            elif choice == 3:
                e.delete_employee()
            elif choice == 4:
                s.update_salary()
            elif choice == 5:
                a.mark_attendance()
            elif choice == 6:
                p.generate_payslip()
            elif choice == 7:
                break