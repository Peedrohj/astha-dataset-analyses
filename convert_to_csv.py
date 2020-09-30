from sas7bdat_converter.converter import batch_to_csv
import pandas as pd 

file_dicts = [
    {
        'sas7bdat_file': 'asthma_national.sas7bdat',
        'export_file': 'example_1.csv',
    },

]

batch_to_csv(file_dicts)

