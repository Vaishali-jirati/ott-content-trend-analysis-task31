-- 1. Movies vs TV Shows count
SELECT type, COUNT(*) AS total_titles
FROM netflix_titles
GROUP BY type;

-- 2. Top 5 release years
SELECT release_year, COUNT(*) AS total_titles
FROM netflix_titles
GROUP BY release_year
ORDER BY total_titles DESC
LIMIT 5;

-- 3. Top 5 ratings
SELECT rating, COUNT(*) AS total_titles
FROM netflix_titles
GROUP BY rating
ORDER BY total_titles DESC
LIMIT 5;

-- 4. Top 5 primary countries
SELECT TRIM(SUBSTRING_INDEX(country, ',', 1)) AS main_country,
       COUNT(*) AS total_titles
FROM netflix_titles
GROUP BY main_country
ORDER BY total_titles DESC
LIMIT 5;

-- 5. Average movie duration (in minutes)
SELECT ROUND(AVG(CAST(REPLACE(duration, ' min', '') AS UNSIGNED)), 2) AS avg_minutes
FROM netflix_titles
WHERE type = 'Movie' AND duration LIKE '%min%';