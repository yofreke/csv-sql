# Run SQL queries against csv tables



## Getting started

- `./setup.py` _This will create a virtualenv, and run pip install.  This only needs to be done once._
- `. env/bin/activate` _Activate the new virtual environment_
- `./main.py` _Run the program_



## Notes

- The name of the tables will be the same as the name of the csv file.
- The same data is a truncated `Sacramentorealestatetransactions.csv` from <https://support.spatialkey.com/spatialkey-sample-csv-data/>.



## Example output

```
$ ./main.py

Running query: SELECT * FROM sampleData LIMIT 10

street                           city              zip  state      beds    baths    sq__ft  type         sale_date                       price    latitude    longitude
-------------------------------  --------------  -----  -------  ------  -------  --------  -----------  ----------------------------  -------  ----------  -----------
3526 HIGH ST                     SACRAMENTO      95838  CA            2        1       836  Residential  Wed May 21 00:00:00 EDT 2008    59222     38.6319     -121.435
51 OMAHA CT                      SACRAMENTO      95823  CA            3        1      1167  Residential  Wed May 21 00:00:00 EDT 2008    68212     38.4789     -121.431
2796 BRANCH ST                   SACRAMENTO      95815  CA            2        1       796  Residential  Wed May 21 00:00:00 EDT 2008    68880     38.6183     -121.444
2805 JANETTE WAY                 SACRAMENTO      95815  CA            2        1       852  Residential  Wed May 21 00:00:00 EDT 2008    69307     38.6168     -121.439
6001 MCMAHON DR                  SACRAMENTO      95824  CA            2        1       797  Residential  Wed May 21 00:00:00 EDT 2008    81900     38.5195     -121.436
5828 PEPPERMILL CT               SACRAMENTO      95841  CA            3        1      1122  Condo        Wed May 21 00:00:00 EDT 2008    89921     38.6626     -121.328
6048 OGDEN NASH WAY              SACRAMENTO      95842  CA            3        2      1104  Residential  Wed May 21 00:00:00 EDT 2008    90895     38.6817     -121.352
2561 19TH AVE                    SACRAMENTO      95820  CA            3        1      1177  Residential  Wed May 21 00:00:00 EDT 2008    91002     38.5351     -121.481
11150 TRINITY RIVER DR Unit 114  RANCHO CORDOVA  95670  CA            2        2       941  Condo        Wed May 21 00:00:00 EDT 2008    94905     38.6212     -121.271
7325 10TH ST                     RIO LINDA       95673  CA            3        2      1146  Residential  Wed May 21 00:00:00 EDT 2008    98937     38.7009     -121.443
```
