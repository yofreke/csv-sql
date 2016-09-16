#! /usr/bin/env python
from src.csv_import import load_file, run_query


# Load the csv file
load_file('./sampleData/realEstate.csv')
load_file('./sampleData/salesData.xlsx')


# Run the query
run_query('''
SELECT *
FROM realEstate
LIMIT 5;
''')

run_query('''
SELECT *
FROM salesdata_sheet1
LIMIT 5;
''')
