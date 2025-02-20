SELECT m.name AS name
FROM Employee e
INNER JOIN Employee m
ON e.managerId = m.id
GROUP BY m.id
HAVING COUNT(m.id) >= 5