if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@transformer
def transform(data, *args, **kwargs):
    data = data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]

    # Create a new column lpep_pickup_date
    data.loc[:, 'lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date

    # Rename columns in Camel Case to Snake Case
    data = data.rename(columns={
        'VendorID': 'vendor_id',
        'RatecodeID': 'ratecode_id',
        'PULocationID': 'pu_location_id',
        'DOLocationID': 'do_location_id',
    })

    return data

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    #assert output is not None, 'The output is undefined'
    assert output['vendor_id'].isin([1, 2]).all(), "Assertion Error: vendor_id is not one of the existing values."
    assert (output['passenger_count'] > 0).all(), "Assertion Error: passenger_count is not greater than 0."
    assert (output['trip_distance'] > 0).all(), "Assertion Error: trip_distance is not greater than 0."

