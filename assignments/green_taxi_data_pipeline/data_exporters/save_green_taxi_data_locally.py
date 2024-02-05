import pyarrow as pa
import pyarrow.parquet as pq
from pandas import DataFrame
import os

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

# Update the variable below
output_folder = './green_taxi_2020_output'

@data_exporter
def export_data_locally(df: DataFrame, **kwargs) -> None:
    # Creating a new date column from the existing datetime column
    #df['tpep_pickup_date'] = df['tpep_pickup_datetime'].dt.date

    table = pa.Table.from_pandas(df)

    # Write to local directory
    pq.write_to_dataset(
        table,
        root_path=output_folder,
        partition_cols=['lpep_pickup_date']
    )




