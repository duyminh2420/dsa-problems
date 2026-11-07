# Write your MySQL query statement below
# find the employees who are high earners in each of the departments.

#find all the employee in each departments with salary from top to bottom 
-- SELECT name as employee_name, salary, department_id
-- FROM Employee
-- WHERE RANK() OVER (PARTITION BY department_id ORDER BY salary)
#Find the name of that department by using join 
WITH ranked AS (
    SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary, 
        DENSE_RANK() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC) AS rnk
    FROM Employee e JOIN Department d ON e.departmentId = d.id
)

SELECT Department, Employee, Salary
FROM ranked
WHERE rnk <= 3 
ORDER BY Department, salary DESC;


#combine those two with subqueries CTEs 
