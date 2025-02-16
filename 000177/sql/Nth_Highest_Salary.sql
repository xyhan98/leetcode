CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    RETURN (
        SELECT salary
        FROM (
            SELECT salary,
                dense_rank() over (ORDER BY salary DESC) AS r
            FROM Employee
        ) AS t
        WHERE r = N
        LIMIT 1
    );
END