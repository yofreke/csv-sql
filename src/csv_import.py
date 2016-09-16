import sqlite3
import pandas
import os
import logging
import sys
from tabulate import tabulate


logging.basicConfig(level='DEBUG')


con = sqlite3.connect(':memory:')


def load_csv(input_file):
    # Read in csv file
    df = pandas.read_csv(input_file)

    # Put csv data in to in-memory database
    table_name = os.path.basename(input_file)
    table_name = table_name[:table_name.find('.')]
    df.to_sql(table_name, con, if_exists='replace', index=False)

    # commit the database, ready for use
    con.commit()


def pp(cursor, data=None, rowlens=0):
    d = cursor.description
    if not d:
        return '#### NO RESULTS ###'
    headers = []
    for dd in d:  # iterate over description
        l = dd[1]
        if not l:
            l = 12  # or default arg ...
        l = max(l, len(dd[0]))  # handle long headers
        headers.append(dd[0])
    table = []
    data = cursor.fetchall()
    for row in data:
        table.append(row)
    return tabulate(table, headers=headers)


def run_query(q):
    # Get the cursor, this will be used for running queries
    cur = con.cursor()

    try:
        # Run the query
        print '\nRunning query: {}'.format(q)
        cur = cur.execute(q)
        print '\n{}'.format(pp(cur))
    except sqlite3.Error as e:
        if con:
            con.rollback()
        print 'Error running query: {}'.format(e)
        sys.exit(1)
