-- get avg temp by city
SELECT city, AVG(value) AS avg_temp
FROM temperatures WHERE city IS NOT NULL
GROUP BY city ORDER BY avg_temp DESC;
