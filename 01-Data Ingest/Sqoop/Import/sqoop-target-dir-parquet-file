--target-dir + parquet

## Step 1
```Shell
sqoop import \
--connect jdbc:mysql://quickstart:3306/retail_db \
--username retail_dba \
--password cloudera \
--table products \
--target-dir /user/cloudera/sqoop/test_target_dir_parquet_file \
--as-parquetfile
```

## Step 2
```Shell
[cloudera@quickstart ~]$ hdfs dfs -ls /user/cloudera/sqoop/test_target_dir_parquet_file
Found 6 items
drwxr-xr-x   - cloudera cloudera          0 2017-11-04 20:43 /user/cloudera/sqoop/test_target_dir_parquet_file/.metadata
drwxr-xr-x   - cloudera cloudera          0 2017-11-04 20:44 /user/cloudera/sqoop/test_target_dir_parquet_file/.signals
-rw-r--r--   1 cloudera cloudera      13909 2017-11-04 20:44 /user/cloudera/sqoop/test_target_dir_parquet_file/3b0f53d9-1fae-4f03-8ce0-0a03200ba11b.parquet
-rw-r--r--   1 cloudera cloudera      16748 2017-11-04 20:44 /user/cloudera/sqoop/test_target_dir_parquet_file/6f806638-4dc8-419d-85fb-a169d4929d2b.parquet
-rw-r--r--   1 cloudera cloudera      16992 2017-11-04 20:44 /user/cloudera/sqoop/test_target_dir_parquet_file/dd01eda9-befc-45d9-a4c3-cfa7cbb96227.parquet
-rw-r--r--   1 cloudera cloudera      13609 2017-11-04 20:44 /user/cloudera/sqoop/test_target_dir_parquet_file/eb4bce23-41a4-44f4-bcf1-029c65ee33e1.parquet
```
