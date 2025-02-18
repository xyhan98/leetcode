SELECT Department, Employee, Salary
FROM (
    SELECT
        d.name AS "Department",
        e.name AS "Employee",
        e.salary AS "Salary",
        rank() over (PARTITION BY d.id ORDER BY e.salary DESC) AS r
    FROM Employee e
    INNER JOIN Department d
    WHERE e.departmentId = d.id
) AS t
WHERE r = 1