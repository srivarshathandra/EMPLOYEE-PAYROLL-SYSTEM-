from db_connection import cursor, db_connect

# 1. CREATE PARENT TABLE FIRST
cursor.execute("""
create table if not exists employees (
    emp_id int auto_increment primary key,
    name VARCHAR(50),
    department VARCHAR(50),
    username VARCHAR(50) UNIQUE,
    password VARCHAR(50)
)
""")

# 2. SALARY TABLE (depends on employees)
cursor.execute("""
create table if not exists salary (
    emp_id int primary key,
    base_salary FLOAT,
    bonus FLOAT,
    FOREIGN KEY (emp_id) references employees(emp_id)
)
""")

# 3. ATTENDANCE TABLE
cursor.execute("""
create table if not exists attendance (
    emp_id int primary key,
    days_present int,
    FOREIGN KEY (emp_id) references employees(emp_id)
)
""")

db_connect.commit()
print("All tables created successfully!")