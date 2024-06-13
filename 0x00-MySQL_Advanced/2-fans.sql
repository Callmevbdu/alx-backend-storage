-- This SQL script ranks country origins of bands ordered by the number of fans

-- The data returned is stored in a result table, called the result-set.
SELECT origin, COUNT(fans) AS nb_fans
	FROM metal_bands
	GROUP BY origin
	ORDER BY nb_fans DESC;
