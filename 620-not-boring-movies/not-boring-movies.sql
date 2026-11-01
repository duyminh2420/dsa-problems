# Write your MySQL query statement below
#report movies with odd numbered ID, description (not boring), ordered by rating dsc 

SELECT *
FROM Cinema
WHERE mod(id, 2) = 1
and description != 'Boring'
ORDER BY rating desc 