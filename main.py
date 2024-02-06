import mysql.connector
from pprint import pprint

# connect to the database
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="password",
  database="hrdatabase"
)

# create a cursor
cursor = mydb.cursor()

# Question 1: What are the names of all employees?
query = "SELECT DISTINCT employee_name FROM employee"
cursor.execute(query)
result = cursor.fetchall()
print("Q1: What are the names of all employees?")
pprint(result)
print()

# Question 2: What is the salary of each employee?
query = "SELECT employee_name, salary FROM employee"
cursor.execute(query)
result = cursor.fetchall()
print("Q2: What is the salary of each employee?")
pprint(result)
print()

# Question 3: What are the names and hire dates of all employees who were hired after 01/01/2020?
query = "SELECT employee_name, hire_date FROM employee WHERE hire_date > '2020-01-01'"
cursor.execute(query)
result = cursor.fetchall()
print("Q3: What are the names and hire dates of all employees who were hired after 01/01/2020?")
pprint(result)
print()

# Question 4: What are the names and department of all employees who work in the Marketing department?
query = "SELECT employee_name FROM employee E INNER JOIN department D ON E.department_id = D.department_id WHERE D.department_name = 'Marketing'"
cursor.execute(query)
result = cursor.fetchall()
print("Q4: What are the names and department of all employees who work in the Marketing department?")
pprint(result)
print()

# Question 5: What are the names and department of all employees who do not work in the Sales department?
query = "SELECT E.employee_name, D.department_name FROM employee E INNER JOIN department D ON E.department_id = D.department_id WHERE D.department_name != 'Sales'"
cursor.execute(query)
result = cursor.fetchall()
print("Q5: What are the names and department of all employees who do not work in the Sales department?")
pprint(result)
print()

# Question 6: What are the names, salary, and hire date of all employees who make more than $60,000 and were hired before 01/01/2022?
query = "SELECT employee_name, salary, hire_date FROM employee WHERE salary > 60000 AND hire_date < '2022-01-01'"
cursor.execute(query)
result = cursor.fetchall()
print("Q6: What are the names, salary, and hire date of all employees who make more than $60,000 and were hired before 01/01/2022?")
pprint(result)
print()

# Question 7: What is the average salary of all employees?
query = "SELECT AVG(salary) FROM employee"
cursor.execute(query)
result = cursor.fetchall()
print("Q7: What is the average salary of all employees?")
pprint(result)
print()

# Question 8: What is the highest salary among all employees?
query = "SELECT MAX(salary) FROM employee"
cursor.execute(query)
result = cursor.fetchall()
print("Q8: What is the highest salary among all employees?")
pprint(result)
print()

# Question 9: What is the total salary of all employees in the Sales and Marketing department?
query = "SELECT SUM(salary) FROM employee E INNER JOIN department D ON E.department_id = D.department_id WHERE D.department_name IN ('Sales', 'Marketing')"
cursor.execute(query)
result = cursor.fetchall()
print("Q9: What is the total salary of all employees in the Sales and Marketing department?")
pprint(result)
print()


# Question 10: How many employees have a salary greater than $80,000?
query = "SELECT COUNT(employee_name) FROM employee WHERE salary > 80000"
cursor.execute(query)
result = cursor.fetchall()
print("Q10: How many employees have a salary greater than $80,000?")
pprint(result)
print()


# Question 11: Find the names of all employees who work in the 'Sales' department.
query = "SELECT E.employee_name FROM employee E INNER JOIN department D ON E.department_id = D.department_id WHERE D.department_name = 'Sales'"
cursor.execute(query)
result = cursor.fetchall()
print("Q11: Find the names of all employees who work in the 'Sales' department.")
pprint(result)
print()

# Question 12: Find the department name, hire date, and salary for employee with the ID of 3.
query = "SELECT D.department_name, E.hire_date, E.salary FROM employee E INNER JOIN department D ON E.department_id = D.department_id WHERE E.employee_id = 3"
cursor.execute(query)
result = cursor.fetchall()
print("Q12: Find the department name, hire date, and salary for employee with the ID of 3.")
pprint(result)
print()

# Question 13: Find the department names and total number of employees in each department.
query = "SELECT D.department_name, COUNT(employee_name) AS employee_count FROM employee E INNER JOIN department D ON E.department_id = D.department_id GROUP BY D.department_name"
cursor.execute(query)
result = cursor.fetchall()
print("Q13: Find the department names and total number of employees in each department.")
pprint(result)
print()

# Question 14: Find the average salary of all employees in the 'Marketing' department.
query = "SELECT AVG(E.salary) AS average_salary FROM employee E INNER JOIN department D on E.department_id = D.department_id WHERE D.department_name = 'Marketing'"
cursor.execute(query)
result = cursor.fetchall()
print("Q14: Find the average salary of all employees in the 'Marketing' department.")
pprint(result)
print()

# Question 15: Find the names and hire dates of all employees who were hired in 2020 or later.
query = "SELECT E.employee_name, E.hire_date FROM employee E WHERE hire_date > '2019-31-12'"
cursor.execute(query)
result = cursor.fetchall()
print("Q15: Find the names and hire dates of all employees who were hired in 2020 or later.")
pprint(result)
print()

# Question 16: Find the employee name, job title, start date, and end date for all job changes.
query = "SELECT E.employee_name, J.job_title, JH.start_date, JH.end_date FROM employee E INNER JOIN job_history JH ON E.employee_id = JH.employee_id INNER JOIN job J ON J.job_id = JH.job_id WHERE JH.end_date != ''"
cursor.execute(query)
result = cursor.fetchall()
print("Q16: Find the employee name, job title, start date, and end date for all job changes.")
pprint(result)
print()

# Question 17: Find the department names and the highest salary for each department.
query = "SELECT D.department_name, MAX(E.salary) FROM employee E INNER JOIN department D ON E.department_id = D.department_id GROUP BY D.department_name"
cursor.execute(query)
result = cursor.fetchall()
print("Q17: Find the department names and the highest salary for each department.")
pprint(result)
print()

# Question 18: Find the total number of employees who have worked in the 'Engineering' department since 2019.
query = "SELECT E.employee_name, COUNT(E.employee_name) num_of_employees FROM employee E INNER JOIN department D ON E.department_id = D.department_id WHERE D.department_name = 'Engineering' AND E.hire_date > '2018-31-12' GROUP BY E.employee_name"
cursor.execute(query)
result = cursor.fetchall()
print("Q18: Find the total number of employees who have worked in the 'Engineering' department since 2019.")
pprint(result)
print()

# Question 19: Find the employee name, department name, and salary for all employees who earn more than their department average.
query = "SELECT E.employee_name, D.department_name, E.salary FROM employee E INNER JOIN department D on E.department_id = D.department_id INNER JOIN (SELECT department_id, AVG(salary) AS avg_salary FROM employee GROUP BY department_id) AS DA ON E.department_id = DA.department_id WHERE E.salary > DA.avg_salary"
cursor.execute(query)
result = cursor.fetchall()
print("Q19: Find the employee name, department name, and salary for all employees who earn more than their department average.")
pprint(result)
print()

# Question 20: Find the department names and the number of employees who have been in each department for more than 2 years.
query = "SELECT department.department_name, COUNT(*) AS num_employees FROM employee INNER JOIN department ON employee.department_id = department.department_id WHERE hire_date <= DATE_SUB(NOW(), INTERVAL 2 YEAR) GROUP BY department.department_name"
cursor.execute(query)
result = cursor.fetchall()
print("Q20: Find the department names and the number of employees who have been in each department for more than 2 years.")
pprint(result)
print()

# Question 21: Retrieve a list of departments along with the total number of employees in each department.
query = "SELECT D.department_name, COUNT(E.employee_id) FROM employee E INNER JOIN department D ON E.department_id = D.department_id GROUP BY department_name;"
cursor.execute(query)
result = cursor.fetchall()
print("Q21: Retrieve a list of departments along with the total number of employees in each department.")
pprint(result)
print()

# Question 22: Find the average salary of employees hired in the year 2022.
query = """
SELECT AVG(E.Salary) AS AvgSalary2022 
FROM employee E 
WHERE YEAR(E.hire_date) = '2022';
"""
cursor.execute(query)
result = cursor.fetchall()
print("Q22: Find the average salary of employees hired in the year 2022.")
pprint(result)
print()

# Question 23: Identify the department with the highest total salary expenditure.
query = """
SELECT D.department_name, SUM(E.salary) 
FROM employee E 
INNER JOIN department D ON E.department_id = D.department_id
GROUP BY department_name ORDER BY SUM(E.salary) DESC;
"""
cursor.execute(query)
result = cursor.fetchall()
print("Q23: Identify the department with the highest total salary expenditure.")
pprint(result)
print()

# Question 24: Retrieve a list of employees who earn more than the average salary in their respective departments.
query = """
SELECT E.employee_name, D.department_name, E.salary 
FROM employee E 
INNER JOIN department D ON E.department_id = D.department_id 
JOIN (
    SELECT DD.department_id, AVG(EE.salary) AS avg_salary 
    FROM employee EE, department DD 
    GROUP BY DD.department_id
) AS avg_salaries ON D.department_id = E.department_id 
WHERE avg_salaries.avg_salary < E.salary;
"""
cursor.execute(query)
result = cursor.fetchall()
print("Q24: Retrieve a list of employees who earn more than the average salary in their respective departments.")
pprint(result)
print()

# Question 25: Find the employee who has the highest salary and the department they belong to.
query = """
SELECT E.employee_name, D.department_name, E.salary 
FROM employee E 
INNER JOIN department D ON E.department_id = D.department_id 
WHERE E.salary = (SELECT MAX(EE.salary) FROM employee EE);
"""
cursor.execute(query)
result = cursor.fetchall()
print("Q25: Find the employee who has the highest salary and the department they belong to.")
pprint(result)
print()


# Question 26: List the employees who have been in their current job for more than three years.
query = """
SELECT e.employee_id, e.employee_name, jh.job_id, j.job_title, jh.start_date 
FROM employee e 
JOIN job_history jh ON e.employee_id = jh.employee_id 
JOIN job j ON jh.job_id = j.job_id 
WHERE TIMESTAMPDIFF(YEAR, jh.start_date, CURRENT_DATE) > 3 AND jh.end_date = '';
"""
cursor.execute(query)
result = cursor.fetchall()
print("Q26: List the employees who have been in their current job for more than three years.")
pprint(result)
print()

# Question 27: Display the department names along with the number of distinct job titles in each department.
query = """
SELECT D.department_name, COUNT(J.job_title) 
FROM employee E 
INNER JOIN department D ON E.department_id = D.department_id
INNER JOIN job_history JH ON E.employee_id = JH.employee_id
INNER JOIN job J ON JH.job_id = J.job_id
GROUP BY D.department_name ORDER BY D.department_name DESC;
"""
cursor.execute(query)
result = cursor.fetchall()
print("Q27: Display the department names along with the number of distinct job titles in each department.")
pprint(result)
print()

# Question 28: Find the job title with the highest number of employees.
query = """
SELECT J.job_title, COUNT(J.job_title) 
FROM employee E
INNER JOIN department D ON E.department_id = D.department_id
INNER JOIN job_history JH ON E.employee_id = JH.employee_id
INNER JOIN job J ON JH.job_id = J.job_id
GROUP BY J.job_title ORDER BY COUNT(J.job_title) DESC LIMIT 1;
"""
cursor.execute(query)
result = cursor.fetchall()
print("Q28: Find the job title with the highest number of employees.")
pprint(result)
print()

# Question 29: List employees who have the same job title as the employee with employee_id = 1.
query = """
SELECT E.employee_name, J.job_title
FROM employee E
JOIN job_history JH ON E.employee_id = JH.employee_id
JOIN job J ON JH.job_id = J.job_id
WHERE J.job_id = (
    SELECT job_id
    FROM job_history
    WHERE employee_id = 1 AND end_date = ''
);
"""
cursor.execute(query)
result = cursor.fetchall()
print("Q29: List employees who have the same job title as the employee with employee_id = 1.")
pprint(result)
print()

# Question 30: Find the department with the fewest employees.
query = """
SELECT D.department_name, COUNT(E.employee_id) AS EmployeeCount
FROM employee E
INNER JOIN department D ON E.department_id = D.department_id
GROUP BY department_name ORDER BY EmployeeCount ASC limit 1;
"""
cursor.execute(query)
result = cursor.fetchall()
print("Q30: Find the department with the fewest employees.")
pprint(result)
print()

# Question 31: Display the employee names and their job titles for employees who were hired after employee with employee_id = 5.
query = """
SELECT E.employee_name, J.job_title 
FROM employee E
INNER JOIN job_history JH ON E.employee_id = JH.employee_id
INNER JOIN job J ON JH.job_id = J.job_id
WHERE JH.start_date > 
    (SELECT start_date FROM 
        job_history WHERE 
        employee_id = 5 AND end_date = '')
"""
cursor.execute(query)
result = cursor.fetchall()
print("Q31: Display the employee names and their job titles for employees who were hired after employee with employee_id = 5.")
pprint(result)
print()

# Question 32: Retrieve the job titles and the total number of employees in each job title, but exclude job titles with fewer than 3 employees.
query = """
SELECT J.job_title, COUNT(E.employee_id) EmployeeCount 
FROM employee E
INNER JOIN job_history JH ON E.employee_id = JH.employee_id
INNER JOIN job J ON JH.job_id = J.job_id 
GROUP BY J.job_title HAVING EmployeeCount > 3;
"""
cursor.execute(query)
result = cursor.fetchall()
print("Q32: Retrieve the job titles and the total number of employees in each job title, but exclude job titles with fewer than 3 employees.")
pprint(result)
print()

# Question 33: Find the departments where the average salary is above the overall average salary across all departments.
query = """
SELECT D.department_name, AVG(E.salary) AS average_salary 
FROM employee E 
INNER JOIN department D ON D.department_id = E.department_id 
GROUP BY D.department_name 
HAVING average_salary > (SELECT AVG(salary) FROM employee);
"""
cursor.execute(query)
result = cursor.fetchall()
print