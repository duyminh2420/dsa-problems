#return fraction for who log in back to the device 
#find the player who logged in back to the device 
WITH first_login AS (
    SELECT
        player_id,
        MIN(event_date) AS first_date
    FROM activity
    GROUP BY player_id
)

SELECT
    ROUND(
        COUNT(DISTINCT a.player_id) * 1.0 /
        (SELECT COUNT(DISTINCT player_id) FROM activity),
        2
    ) AS fraction
FROM activity a
JOIN first_login f
    ON a.player_id = f.player_id
    AND a.event_date = DATE_ADD(f.first_date, INTERVAL 1 DAY);

