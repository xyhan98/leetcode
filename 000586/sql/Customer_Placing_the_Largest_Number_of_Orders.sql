SELECT customer_number
FROM (
    SELECT customer_number, COUNT(order_number) AS c
    FROM Orders
    GROUP BY customer_number
    ORDER BY c DESC
    LIMIT 1
) AS t