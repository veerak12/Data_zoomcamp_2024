Question 3. Count records
How many taxi trips were totally made on September 18th 2019?

Tip: started and finished on 2019-09-18.

## sql query

"SELECT COUNT(*)
FROM green_taxi_data
WHERE DATE(lpep_pickup_datetime) = '2019-09-18' AND DATE(lpep_dropoff_datetime) = '2019-09-18';"

## Answer = 15612

Question 4. Largest trip for each day
Which was the pick up day with the largest trip distance Use the pick up time for your calculations.

2019-09-18
2019-09-16
2019-09-26
2019-09-21

## sql query
"SELECT
    DATE(lpep_pickup_datetime) AS pickup_day,
    MAX(trip_distance) AS largest_trip_distance
FROM
    green_taxi_data
WHERE
    DATE(lpep_pickup_datetime) IN ('2019-09-18', '2019-09-16', '2019-09-26', '2019-09-21')
GROUP BY
    pickup_day;"

## Answer 2019-09-26

Question 5. Three biggest pick up Boroughs
Consider lpep_pickup_datetime in '2019-09-18' and ignoring Borough has Unknown

Which were the 3 pick up Boroughs that had a sum of total_amount superior to 50000?

"Brooklyn" "Manhattan" "Queens"
"Bronx" "Brooklyn" "Manhattan"
"Bronx" "Manhattan" "Queens"
"Brooklyn" "Queens" "Staten Island"

## sql query
"SELECT
    tz."Borough",
    SUM(gt.total_amount) AS total_amount_sum
FROM
    green_taxi_data gt
JOIN
    taxi_zone_lookup tz ON gt."PULocationID" = tz."LocationID"
WHERE
    DATE(gt.lpep_pickup_datetime) = '2019-09-18'
    AND tz."Borough" != 'Unknown'
GROUP BY
    tz."Borough"
HAVING
    SUM(gt.total_amount) > 50000
ORDER BY
    total_amount_sum DESC
LIMIT 3;"

## Answer "Brooklyn" "Manhattan" "Queens"

Question 6. Largest tip
For the passengers picked up in September 2019 in the zone name Astoria which was the drop off zone that had the largest tip? We want the name of the zone, not the id.

Note: it's not a typo, it's tip , not trip

Central Park
Jamaica
JFK Airport
Long Island City/Queens Plaza

## SQL QUERY

"WITH AstoriaPickups AS (
    SELECT
        gt.*,
        tz_drop."Zone" AS dropoff_zone_name
    FROM
        green_taxi_data gt
    JOIN
        taxi_zone_lookup tz_pickup ON gt."PULocationID" = tz_pickup."LocationID"
    JOIN
        taxi_zone_lookup tz_drop ON gt."DOLocationID" = tz_drop."LocationID"
    WHERE
        tz_pickup."Zone" = 'Astoria'
        AND DATE(gt.lpep_pickup_datetime) BETWEEN '2019-09-01' AND '2019-09-30'
)
SELECT
    dropoff_zone_name,
    MAX(tip_amount) AS largest_tip_amount
FROM
    AstoriaPickups
GROUP BY
    dropoff_zone_name
ORDER BY
    largest_tip_amount DESC
LIMIT 1;"

## Answer "JFK Airport"