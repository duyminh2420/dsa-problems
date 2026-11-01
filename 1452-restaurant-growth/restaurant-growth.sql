# Write your MySQL query statement below
#date, amount moving average of how much the customer paid in a seven days window (current day + 6 days before)
#ORDER BY visited_on asc
SELECT visited_on,
(
    SELECT SUM(amount)
    FROM customer 
    WHERE visited_on BETWEEN DATE_SUB(c.visited_on, INTERVAL 6 DAY) AND c.visited_on
) AS amount,
ROUND((
    SELECT SUM(amount) / 7
    FROM customer 
    WHERE visited_on BETWEEN DATE_SUB(c.visited_on, INTERVAL 6 DAY) AND c.visited_on
),2) AS average_amount
FROM customer c 
WHERE visited_on >= (
    SELECT DATE_ADD(MIN(visited_on), INTERVAL 6 DAY )
    FROM customer 
)
GROUP BY visited_on;