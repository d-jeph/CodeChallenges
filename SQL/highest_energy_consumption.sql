/*
Find the date with the highest total energy consumption from the Meta/Facebook data centers. 
Output the date along with the total energy consumption across all data centers.

Tables: fb_eu_energy, fb_asia_energy, fb_na_energy

fb_eu_energy
date: datetime
consumption: int

fb_asia_energy
date:datetime
consumption:int
*/

SELECT date,consumption 
FROM
(
    SELECT date, SUM(consumption) AS consumption,
    DENSE_RANK() OVER(ORDER BY SUM(consumption) DESC) AS rank
    FROM
    (
        SELECT * FROM FB_EU_ENERGY
        UNION ALL
        SELECT * FROM FB_ASIA_ENERGY
        UNION ALL
        SELECT * FROM FB_NA_ENERGY
    ) A
    GROUP BY DATE
) A
WHERE RANK = 1