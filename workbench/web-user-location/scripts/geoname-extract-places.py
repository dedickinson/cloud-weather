#!/usr/bin/env python3

import pandas as pd
import numpy as np
import pycountry

if __name__ == "__main__":
    data_file = 'data/geonames.txt'

    headers = [
        'geonameid',
        'name',
        'asciiname',
        'alternatenames',
        'lat',
        'long',
        'feature_class',
        'feature_code',
        'country_code',
        'cc2',
        'admin1_code',
        'admin2_code',
        'admin3_code',
        'admin4_code',
        'population',
        'elevation',
        'dem',
        'timezone',
        'modification_date'
    ]

    df = pd.read_csv(data_file,
                     sep='\t',
                     header=0,
                     names=headers,
                     index_col=0,
                     low_memory=False,
                     usecols=['geonameid', 'country_code', 'name', 'lat', 'long', 'timezone', 'feature_class', 'feature_code'])
                     
    df = df[(df['feature_class'] == 'P')]

    df['country'] = df.apply(
        lambda row: pycountry.countries.get(alpha_2=row['country_code']).name, axis=1)

    with open("tmp/locations.json", 'w') as f:
        f.write(df.to_json(orient='records'))

    print('-' * 79)
    print(df.info())
    print('-' * 79)
    print(df.describe())
    print('-' * 79)
    print(df.head(5))
    print('-' * 79)
