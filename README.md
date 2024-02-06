## SQL Scripts
This Python code contains SQL queries to retrieve information from a database of employees. 
# TABLES: 
- employee: employee_id, employee_name, department, hire_date, salary
- department: department_id, department_name
- job: job_id, job_title
- job_history: employee_id, job_id, start_date, end_date

## Questions:
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

# Retrieve a list of departments along with the total number of employees in each department.
`SELECT D.department_name, COUNT(E.employee_id) FROM employee E INNER JOIN department D ON E.department_id = D.department_id GROUP BY department_name;`

# Find the average salary of employees hired in the year 2022.
`SELECT AVG(E.Salary) AS AvgSalary2022 FROM employee E WHERE YEAR(E.hire_date) = '2022';`

# Identify the department with the highest total salary expenditure.
`SELECT D.department_name, SUM(E.salary) FROM employee E  INNER JOIN department D ON E.department_id = D.department_id GROUP BY department_name ORDER BY SUM(E.salary) DESC;`

# Retrieve a list of employees who earn more than the average salary in their respective departments.
`SELECT E.employee_name, D.department_name, E.salary FROM employee E INNER JOIN department D ON E.department_id = D.department_id JOIN (SELECT DD.department_id, AVG(EE.salary) AS avg_salary FROM employee EE, department DD GROUP BY DD.department_id) AS avg_salaries ON D.department_id = E.department_id WHERE avg_salaries.avg_salary < E.salary;`

# Find the employee who has the highest salary and the department they belong to.
`SELECT E.employee_name, D.department_name, E.salary FROM employee E INNER JOIN department D ON E.department_id = D.department_id WHERE E.salary = (SELECT MAX(EE.salary) FROM employee EE);`

# List the employees who have been in their current job for more than three years.
`SELECT e.employee_id, e.employee_name, jh.job_id, j.job_title, jh.start_date FROM employee e JOIN job_history jh ON e.employee_id = jh.employee_id JOIN job j ON jh.job_id = j.job_id WHERE TIMESTAMPDIFF(YEAR, jh.start_date, CURRENT_DATE) > 3 AND jh.end_date = '';`

# Display the department names along with the number of distinct job titles in each department.
`SELECT D.department_name, COUNT(J.job_title) FROM employee E INNER JOIN department D ON E.department_id = D.department_idINNER JOIN job_history JH ON E.employee_id = JH.employee_idINNER JOIN job J ON JH.job_id = J.job_id GROUP BY D.department_name ORDER BY D.department_name DESC;`

# Find the job title with the highest number of employees.
`SELECT J.job_title, COUNT(J.job_title) FROM employee E INNER JOIN department D ON E.department_id = D.department_id INNER JOIN job_history JH ON E.employee_id = JH.employee_id INNER JOIN job J ON JH.job_id = J.job_id GROUP BY J.job_title ORDER BY COUNT(J.job_title) DESC LIMIT 1;`\

# List employees who have the same job title as the employee with employee_id = 1.
`SELECT E.employee_name, J.job_title FROM employee E JOIN job_history JH ON E.employee_id = JH.employee_id JOIN job J ON JH.job_id = J.job_id WHERE J.job_id = (SELECT job_id FROM job_history WHERE employee_id = 1 AND end_date = '');`

# Find the department with the fewest employees.
`SELECT D.department_name, COUNT(E.employee_id) AS EmployeeCount FROM employee E INNER JOIN department D ON E.department_id = D.department_id GROUP BY department_name ORDER BY EmployeeCount ASC limit 1`

# Display the employee names and their job titles for employees who were hired after employee with employee_id = 5.
`SELECT E.employee_name, J.job_title FROM employee E INNER JOIN job_history JH ON E.employee_id = JH.employee_id INNER JOIN job J ON JH.job_id = J.job_id WHERE JH.start_date > (SELECT start_date FROM job_history WHERE employee_id = 5 AND end_date = '')`

# Retrieve the job titles and the total number of employees in each job title, but exclude job titles with fewer than 3 employees.
`SELECT J.job_title, COUNT(E.employee_id) EmployeeCount FROM employee E INNER JOIN job_history JH ON E.employee_id = JH.employee_id INNER JOIN job J ON JH.job_id = J.job_id GROUP BY J.job_title HAVING EmployeeCount > 3`

# Find the departments where the average salary is above the overall average salary across all departments. Display the department_name and the corresponding average_salary.
`SELECT D.department_name, AVG(E.salary) AS average_salary FROM employee E INNER JOIN department D ON D.department_id = E.department_id GROUP BY D.department_name HAVING average_salary > (SELECT AVG(salary) FROM employee);`

# Create a report that displays the employee_id, employee_name, and a column called employment_status indicating 'Full-Time' for employees hired before 2022 and 'Part-Time' for employees hired in or after 2022.
`SELECT E.employee_id, E.employee_name, CASE WHEN YEAR(JH.start_date) < 2022 THEN "Full-Time" ELSE "Part-Time" END AS employment_status FROM employee E INNER JOIN job_history JH ON E.employee_id = JH.employee_id WHERE JH.end_date = '';`

# List all employees with their employee_id, job_title, employee_name, and a column called job_tenure that categorizes employees into 'New' if hired in 2023, 'Experienced' if hired between 2019 and 2022, and 'Veteran' if hired before 2019.
`SELECT E.employee_id, J.job_title, E.employee_name, CASE WHEN YEAR(JH.start_date) = 2023 THEN "New" WHEN YEAR(JH.start_date) > 2018 AND YEAR(JH.start_date) < 2023 THEN "Experienced" WHEN YEAR(JH.start_date) < 2019 THEN "Veteran" ELSE NULL END AS job_tenure FROM employee E INNER JOIN job_history JH ON E.employee_id = JH.employee_id INNER JOIN job J ON JH.job_id = J.job_id;`

# Display the employee_id, employee_name, and a column called job_type indicating 'Technical' for employees in the 'Engineering' department and 'Non-Technical' for employees in other departments.
`SELECT E.employee_id, E.employee_name, CASE WHEN J.job_title LIKE '%Engineer' THEN 'Technical' ELSE 'Non-Technical' END AS job_type FROM employee E INNER JOIN job_history JH ON E.employee_id = JH.employee_id INNER JOIN job J ON JH.job_id = J.job_id WHERE JH.end_date = '';`

# Create a report that includes the employee_id, employee_name, and a column named job_security that categorizes employees as 'Secure' if their job title contains 'Manager' and 'Insecure' otherwise.
`SELECT E.employee_id, E.employee_name, CASE WHEN J.job_title LIKE '%Manager' THEN 'Secure' ELSE 'Insecure' END AS job_security FROM employee E INNER JOIN job_history JH ON E.employee_id = JH.employee_id INNER JOIN job J ON JH.job_id = J.job_id WHERE JH.end_date = '';`