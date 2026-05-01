from db_connection import cursor, db_connect

# EMPLOYEES TABLE 
employees_table = """
create table if not exists employees (
    emp_id INT PRIMARY KEY ,
    name VARCHAR(50),
    department VARCHAR(50)
)
"""
cursor.execute(employees_table)

#  SALARY TABLE 

salary_table = """
create table if not exists salary (
    emp_id INT PRIMARY KEY,
    base_salary FLOAT,
    bonus FLOAT,
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id)
)
"""
cursor.execute(salary_table)

# ATTENDANCE TABLE 

attendance_table = """
create table if not exists attendance (
    emp_id INT PRIMARY KEY,
    days_present INT,
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id)
)
"""
cursor.execute(attendance_table)

# Commit changes
db_connect.commit()

print("All tables created successfully!")


