-- SELECT e2.salary AS SecondHighestSalary
-- FROM Employee e1
-- LEFT JOIN Employee e2
-- ON e1.salary > e2.salary
-- ORDER BY e1.salary DESC, e2.salary DESC
-- LIMIT 1

SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary != (SELECT MAX(salary) FROM Employee)