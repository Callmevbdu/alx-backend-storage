-- This SQL script ranks country origins of bands ordered by the number of fans

-- The data returned is stored in a result table, called the result-set.
SELECT 
    -- 'origin' is the column that contains the country of origin of the bands.
    origin, 
    
    -- 'AS nb_fans' is used to rename the column in the output.
    COUNT(fans) AS nb_fans
FROM 
    -- Here, we are selecting data from the 'metal_bands' table.
    metal_bands

-- specified columns into aggregated data.
GROUP BY 
    -- We are grouping the data by 'origin'.
    origin

ORDER BY 
    -- We are sorting the data by 'nb_fans' in descending order ('DESC').
    nb_fans DESC;
