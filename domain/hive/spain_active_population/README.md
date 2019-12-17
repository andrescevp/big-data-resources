# Create table from parquet file
```
create external table EPAP (CICLO integer)
STORED AS PARQUET
LOCATION '/tmp/data/EPA_2019T2.csv.parquet';
```
