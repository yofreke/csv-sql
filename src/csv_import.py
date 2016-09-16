import os
import logging
import sys
import sqlite3
import tempfile
import csv

import pandas
import tabulate
import openpyxl
import slugify


logging.basicConfig(level='INFO')
LOGGER = logging.getLogger('csv_import')


con = sqlite3.connect(':memory:')


def _get_table_name(input_file):
    return os.path.splitext(os.path.basename(input_file))[0]


def _load_xlsx(input_file):
    LOGGER.info('Converting xlsx: %s', input_file)
    wb = openpyxl.load_workbook(filename=input_file, read_only=True)
    for ws in wb.worksheets:
        sheet_title = slugify.slugify('{} {}'.format(
            _get_table_name(input_file),
            ws.title
        ), separator='_')
        LOGGER.info('> Found sheet: %s', sheet_title)

        # Write to tempfile
        out_file = tempfile.SpooledTemporaryFile(
            max_size=1000 * 1000 * 16  # 16mb
        )
        wr = csv.writer(
            out_file,
            quoting=csv.QUOTE_MINIMAL,
            lineterminator='\n',
            escapechar='\\'
        )

        for row in ws.iter_rows(min_row=1):
            cells = []
            for cell in row:
                cells.append(cell.value)
            wr.writerow(cells)
        # Rewind file
        out_file.seek(0)
        # Read from tempfile
        _load_csv(out_file, table_name=sheet_title)


def _load_csv(input_file, table_name=None):
    # Read in csv file
    df = pandas.read_csv(input_file)

    if table_name is None:
        table_name = _get_table_name(input_file)

    # Put csv data in to in-memory database
    df.to_sql(table_name, con, if_exists='replace', index=False)

    # commit the database, ready for use
    con.commit()


LOADER_MAP = {
    '.xlsx': _load_xlsx,
    '.csv': _load_csv
}

def load_file(input_file):
    ext = os.path.splitext(input_file)[1]
    LOGGER.info('Loading file: %s', input_file)
    if ext in LOADER_MAP:
        return LOADER_MAP[ext](input_file)
    else:
        raise Exception('Unknown file extension: {}'.format(ext))


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
    return tabulate.tabulate(table, headers=headers)


def run_query(q):
    # Get the cursor, this will be used for running queries
    cur = con.cursor()

    try:
        # Run the query
        print '\n\nRunning query: {}'.format(q)
        cur = cur.execute(q)
        print pp(cur)
    except sqlite3.Error as e:
        if con:
            con.rollback()
        print 'Error running query: {}'.format(e)
        sys.exit(1)
