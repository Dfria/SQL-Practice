# SQL Scripts
This Python code contains SQL queries to retrieve information from a database of employees. 
# TABLES: 
- employee: employee_id, employee_name, department, hire_date, salary
- department: department_id, department_name
- job: job_id, job_title
- job_history: employee_id, job_id, start_date, end_date
The questions asked in the code and their corresponding SQL scripts are:

# What are the names of all employees?
`SELECT DISTINCT employee_name FROM employee`

# What is the salary of each employee?
`SELECT employee_name, salary FROM employee`

# What are the names and hire dates of all employees who were hired after 01/01/2020?
`SELECT employee_name, hire_date FROM employee WHERE hire_date > '2020-01-01'`

# What are the names and department of all employees who work in the Marketing department?
`SELECT employee_name FROM employee E INNER JOIN department D ON E.department_id = D.department_id WHERE D.department_name = 'Marketing'`

# What are the names and department of all employees who do not work in the Sales department?
`SELECT E.employee_name, D.department_name FROM employee E INNER JOIN department D ON E.department_id = D.department_id WHERE D.department_name != 'Sales'`

# What are the names, salary, and hire date of all employees who make more than $60,000 and were hired before 01/01/2022?
`SELECT employee_name, salary, hire_date FROM employee WHERE salary > 60000 AND hire_date < '2022-01-01'`

# What is the average salary of all employees?
`SELECT AVG(salary) FROM employee`

# What is the highest salary among all employees?
`SELECT MAX(salary) FROM employee`

# What is the total salary of all employees in the Sales and Marketing department?
`SELECT SUM(salary) FROM employee E INNER JOIN department D ON E.department_id = D.department_id WHERE D.department_name IN ('Sales', 'Marketing')`

# How many employees have a salary greater than $80,000?
`SELECT COUNT(employee_name) FROM employee WHERE salary > 80000`

# Find the names of all employees who work in the 'Sales' department.
`SELECT E.employee_name FROM employee E INNER JOIN department D ON E.department_id = D.department_id WHERE D.department_name = 'Sales'`

# Find the department name, hire date, and salary for employee with the ID of 3.
`SELECT D.department_name, E.hire_date, E.salary FROM employee E INNER JOIN department D ON E.department_id = D.department_id WHERE E.employee_id = 3`

# Find the department names and total number of employees in each department.
`SELECT D.department_name, COUNT(employee_name) AS employee_count FROM employee E INNER JOIN department D ON E.department_id = D.department_id GROUP BY D.department_name`

# Find the average salary of all employees in the 'Marketing' department.
`SELECT AVG(E.salary) AS average_salary FROM employee E INNER JOIN department D on E.department_id = D.department_id WHERE D.department_name = 'Marketing'`

# Find the names and hire dates of all employees who were hired in 2020 or later.
`SELECT E.employee_name, E.hire_date FROM employee E WHERE hire_date > '2019-31-12'`

# Find the employee name, job title, start date, and end date for all job changes.
`SELECT E.employee_name, J.job_title, JH.start_date, JH.end_date FROM employee E INNER JOIN job_history JH ON E.employee_id = JH.employee_id INNER JOIN job J ON J.job_id = JH.job_id WHERE JH.end_date != ''`

# Find the department names and the highest salary for each department.
`SELECT D.department_name, MAX(E.salary) FROM employee E INNER JOIN department D ON E.department_id = D.department_id GROUP BY D.department_name`

# Find the total number of employees who have worked in the 'Engineering' department since 2019.
`SELECT E.employee_name, COUNT(E.employee_name) num_of_employees FROM employee E INNER JOIN department D ON E.department_id = D.department_id WHERE D.department_name = 'Engineering' AND E.hire_date > '2018-31-12' GROUP BY E.employee_name`

# Find the employee name, department name, and salary for all employees who earn more than their department average.
`SELECT E.employee_name, D.department_name, E.salary FROM employee E INNER JOIN department D on E.department_id = D.department_id INNER JOIN (SELECT department_id, AVG(salary) AS avg_salary FROM employee GROUP BY department_id) AS DA ON E.department_id = DA.department_id WHERE E.salary > DA.avg_salary`

# Find the department names and the number of employees who have been in each department for more than 2 years.
`SELECT department.department_name, COUNT(*) AS num_employees FROM employee INNER JOIN department ON employee.department_id = department.department_id WHERE hire_date <= DATE_SUB(NOW(), INTERVAL 2 YEAR) GROUP BY department.department_name`







