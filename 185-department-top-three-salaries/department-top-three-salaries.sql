# Write your MySQL query statement below
#find the employees who are high earners in each of the departments.

#JOIN 2 table to find who in which department
SELECT d.name AS Department, e1.name AS Employee, e1.salary AS Salary
FROM Employee e1
JOIN Department d
ON e1.departmentId = d.id 
WHERE 
    3 > (SELECT COUNT(DISTINCT e2.salary)
    FROM Employee e2
    WHERE e2.salary > e1.salary AND e1.departmentID = e2.departmentId
    )
