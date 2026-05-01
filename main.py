
from Add_employees import Employee
from payroll import Payroll
from attendance import Attendance
from payslip import Payslip

e = Employee()
p = Payroll()
a = Attendance()
ps = Payslip()

print("1. Add Employee")
print("2. View Employees")
print("3. Delete Employee")
print("4. Update Salary")
print("5. Mark Attendance")
print("6. Generate Payslip")

choice = int(input("Enter choice: "))

if choice == 1:
    e.add_employee()

elif choice == 2:
    e.view_employees()

elif choice == 3:
    e.delete_employee()

elif choice == 4:
    p.update_salary()

elif choice == 5:
    a.mark_attendance()

elif choice == 6:
    ps.generate_payslip()