# Run SQL queries against csv tables



## Getting started

- `./setup.py` _This will create a virtualenv, and run pip install.  This only needs to be done once._
- `. env/bin/activate` _Activate the new virtual environment_
- `./main.py` _Run the program_



## Notes

- The name of the tables will be the same as the name of the csv file.
- You can load more than one csv file, each will be loaded in to its own table.
- The sample data "realEstate.csv" is a truncated `Sacramentorealestatetransactions.csv` from <https://support.spatialkey.com/spatialkey-sample-csv-data/>.
- The sample data "salesData.xlsx" is from <reference1.mapinfo.com/software/anysite/english_AU/.../Sample-Sales-Data.xlsx>.




## Example output

```
$ ./main.py
INFO:csv_import:Loading file: ./sampleData/realEstate.csv
INFO:csv_import:Loading file: ./sampleData/salesData.xlsx
INFO:csv_import:Converting xlsx: ./sampleData/salesData.xlsx
INFO:csv_import:> Found sheet: salesdata_sheet1


Running query:
SELECT *
FROM realEstate
LIMIT 5;

street            city          zip  state      beds    baths    sq__ft  type         sale_date                       price    latitude    longitude
----------------  ----------  -----  -------  ------  -------  --------  -----------  ----------------------------  -------  ----------  -----------
3526 HIGH ST      SACRAMENTO  95838  CA            2        1       836  Residential  Wed May 21 00:00:00 EDT 2008    59222     38.6319     -121.435
51 OMAHA CT       SACRAMENTO  95823  CA            3        1      1167  Residential  Wed May 21 00:00:00 EDT 2008    68212     38.4789     -121.431
2796 BRANCH ST    SACRAMENTO  95815  CA            2        1       796  Residential  Wed May 21 00:00:00 EDT 2008    68880     38.6183     -121.444
2805 JANETTE WAY  SACRAMENTO  95815  CA            2        1       852  Residential  Wed May 21 00:00:00 EDT 2008    69307     38.6168     -121.439
6001 MCMAHON DR   SACRAMENTO  95824  CA            2        1       797  Residential  Wed May 21 00:00:00 EDT 2008    81900     38.5195     -121.436


Running query:
SELECT *
FROM salesdata_sheet1
LIMIT 5;

  Postcode    Sales_Rep_ID  Sales_Rep_Name      Year    Value
----------  --------------  ----------------  ------  -------
      2121             456  Jane                2011  84219.5
      2092             789  Ashish              2012  28322.2
      2128             456  Jane                2013  81879
      2073             123  John                2011  44491.1
      2134             789  Ashish              2012  71837.7
```
