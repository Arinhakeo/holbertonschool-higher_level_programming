-- Script that lists the number of records for each score
SELECT score, COUNT(*) as number
FROM second_table
GROUP BY score
ORDER BY number DESC;
