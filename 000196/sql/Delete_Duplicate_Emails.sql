DELETE FROM Person
WHERE id NOT IN (
    SELECT id
    FROM (
        SELECT id,
            rank() over (PARTITION BY email ORDER BY id) AS r
        FROM Person
    ) AS t
    WHERE r = 1
)