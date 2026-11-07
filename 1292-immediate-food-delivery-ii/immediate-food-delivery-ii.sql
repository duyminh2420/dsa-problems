# Write your MySQL query statement below
#find percentage of immediate order in the first order of all customers 

#1:first order of all customers 
#2:immediate order in the first orders
#3: get percentage and round to 2 decimal

SELECT round(avg(order_date = customer_pref_delivery_date) * 100, 2) as immediate_percentage
FROM delivery 
WHERE (customer_id, order_date) in (
    SELECT customer_id, min(order_date)
    FROM delivery
    GROUP BY customer_id
)