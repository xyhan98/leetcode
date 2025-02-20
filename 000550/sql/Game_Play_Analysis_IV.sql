SELECT ROUND(COUNT(player_id) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
FROM (
    SELECT
        a1.player_id AS player_id,
        a1.event_date AS date1,
        a2.event_date AS date2,
        rank() over (PARTITION BY a1.player_id ORDER BY a1.event_date) AS r
    FROM Activity a1
    LEFT JOIN Activity a2
    ON a1.player_id = a2.player_id
    AND DATEDIFF(a1.event_date, a2.event_date) = -1
) AS t
WHERE date2 IS NOT NULL
AND r = 1