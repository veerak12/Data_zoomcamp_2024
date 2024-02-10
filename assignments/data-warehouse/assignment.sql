-- Active: 1705746@ny_taxi@public
SELECT COUNT(*) FROM green_taxi_data_2022;
-- 840402

-- For the regular table
EXPLAIN ANALYZE SELECT COUNT(DISTINCT "PULocationID") AS distinct_count
FROM green_taxi_data_2022;
-- 258
-- 0 MB for the External Table and 6.41 MB for the Materialized Table.


SELECT count(fare_amount) FROM green_taxi_data_2022
WHERE fare_amount =0;
--1622

EXPLAIN ANALYZE SELECT DISTINCT "PULocationID"
FROM green_taxi_data_2022
WHERE lpep_pickup_datetime >= '2022-06-01' AND lpep_pickup_datetime <= '2022-06-30';

-- 12.82 MB for non-partitioned table and 1.12 MB for the partitioned table

--4
-- Partition by lpep_pickup_datetime Cluster on PUlocationID

--6
-- GCP BUCKET

--7
--TRUE