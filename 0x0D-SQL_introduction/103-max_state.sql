-- select top temp of state ordered by state
SELECT state, MAX(value) AS max_temp
FROM temperatures
WHERE state IS NOT NULL
GROUP BY state
ORDER BY state;
