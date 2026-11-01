# Write your MySQL query statement below
#find the percentage of immediate orders in the first orders of all customers, rounded to 2 decimal places.

#immediate orders in the first orders of all customers

SELECT round(avg(order_date = customer_pref_delivery_date) * 100, 2) as immediate_percentage
FROM delivery
WHERE (customer_id, order_date) in (
    SELECT customer_id, min(order_date)
    FROM delivery
    GROUP BY customer_id 
)

