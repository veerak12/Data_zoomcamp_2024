
docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v /mnt/d/data_zoomcamp_2024/ingesting_data/ny_taxi_postgres_data:/var/lib/postgresql/data \
  -p 5432:5432 \
  postgres:13

## the above docker image has been failed due to permissions issues..so i have created a local folder inside the docker volumes so that it can take of the data

  Docker - Could not change permissions of directory "/var/lib/postgresql/data": Operation not permitted 

# CCW
The files belonging to this database system will be owned by user "postgres".
This use The database cluster will be initialized with locale "en_US.utf8".
The default databerrorase encoding has accordingly been set to "UTF8".
xt search configuration will be set to "english".

Data page checksums are disabled.
fixing permissions on existing directory /var/lib/postgresql/data ... initdb: 
error: could not change permissions of directory "/var/lib/postgresql/data": Operation not permitted  volume
One way to solve this issue is to create a local docker volume and map it to postgres data directory /var/lib/postgresql/data
The input dtc_postgres_volume_local must match in both commands below

## solution 
$ docker volume create --name dtc_postgres_volume_local -d local

docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v dtc_postgres_volume_local:/var/lib/postgresql/data \
  -p 5432:5432 \
  postgres:13


To verify the above command works in (WSL2 Ubuntu 22.04, verified 2024-Jan), go to the Docker Desktop app and look under Volumes - dtc_postgres_volume_local would be listed there. The folder ny_taxi_postgres_data would however be empty, since we used an alternative config.

## An alternate error could be:

initdb: error: directory "/var/lib/postgresql/data" exists but is not empty
If you want to create a new database system, either remove or empthe directory "/var/lib/postgresql/data" or run initdb
witls

#################################################################################################
## commands
using "wget" command we can download the files in linux

Since it is a big file save the first 100 lines by using the following command

  -- head -n 100 yellow_tripdata_2021-01.csv > yellow_100.csv

Use the following command by counting the number of lines
  -- wc -l yellow_tripdata_2021-01.csv

## look for the schema using pandas io
   -- print(pd.io.sql.get_schema(df,name = 'yellow_taxi_data'))
   output

   CREATE TABLE "yellow_taxi_data" (
"VendorID" INTEGER,
  "tpep_pickup_datetime" TEXT,
  "tpep_dropoff_datetime" TEXT,
  "passenger_count" INTEGER,
  "trip_distance" REAL,
  "RatecodeID" INTEGER,
  "store_and_fwd_flag" TEXT,
  "PULocationID" INTEGER,
  "DOLocationID" INTEGER,
  "payment_type" INTEGER,
  "fare_amount" REAL,
  "extra" REAL,
  "mta_tax" REAL,
  "tip_amount" REAL,
  "tolls_amount" REAL,
  "improvement_surcharge" REAL,
  "total_amount" REAL,
  "congestion_surcharge" REAL
)

## run the pgadmin

docker run -it \
    -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
    -e PGADMIN_DEFAULT_PASSWORD="root" \
    -p 8080:80 \
    dpage/pgadmin4


## unable to connect the pgadmin to pg-database
## Creating network

  -- docker network create pg-network

docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v dtc_postgres_volume_local:/var/lib/postgresql/data \
  -p 5432:5432 \
  --network=pg-network \
  --name pg-database \
  postgres:13

#pg-admin

docker run -it \
  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
  -e PGADMIN_DEFAULT_PASSWORD="root" \
  -p 8080:80 \
  --network=pg-network \
  --name pg-admin \
  dpage/pgadmin4


## running the python script with paramaters
python ingest_data.py \
--user=root \
--password=root \
--host=localhost \
--port=5432 \
--db=ny_taxi \
--table_name=yellow_taxi_trips \
--url="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"

