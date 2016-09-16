#! /usr/bin/env python
from src.csv_import import load_csv, run_query

# Load the csv file
load_csv('./sampleData.csv')

# Run the query
run_query('''
SELECT *
FROM sampleData
LIMIT 10;
''')
