-- This SQL script ranks country origins of bands ordered by the number of fans

SELECT 
    origin, 
    COUNT(fans) AS nb_fans
FROM 
    metal_bands
GROUP BY 
    origin
ORDER BY 
    nb_fans DESC;
