-- Select bands with the Glam rock style
-- Calculate the lifespan for each band with the Glam rock style
-- Order the result set by the calculated lifespan in descending order

SELECT band_name, COALESCE(split, 2022) - formed AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;