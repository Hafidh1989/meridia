import pandas as pd
import pytest

def test_read_csv():
    csv_file = 'field_data.csv'

    df = pd.read_csv(csv_file, header=None)
    df.columns = ['Farmer ID','Farm Name','GPS Latitude','GPS Longitude','Region','Village'
        ,'Farm Size (Ha)','Deforestation Date']

    missing_value = df['Farmer ID'].isnull().sum()
    assert missing_value == 0, missing_value

    row = 0
    for val in df['Farmer ID']:
        if row != 0:
            if val:
                assert len(val) != 0, f"Found missing data on row {row}"
        row = row + 1
