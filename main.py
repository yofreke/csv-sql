#! /usr/bin/env python
from src.csv_import import load_csv, run_query

# Convert csv to sql
load_csv('./sampleData.csv')

# Run the query
run_query('SELECT * FROM sampleData LIMIT 10')
