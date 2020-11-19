-- Max value
--  MAX temperature of each state
SELECT DISTINCT(state), MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state;
