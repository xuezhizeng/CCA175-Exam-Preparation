--target-dir + avro

## Step 1
```Shell
sqoop import \
--connect jdbc:mysql://quickstart:3306/retail_db \
--username retail_dba \
--password cloudera \
--table products \
--target-dir /user/cloudera/sqoop/test-target-dir-avro-file \
--as-avrodatafile
```
## Step 2
```Shell
[cloudera@quickstart ~]$ hdfs dfs -ls /user/cloudera/sqoop/test-target-dir-avro-file
Found 5 items
-rw-r--r--   1 cloudera cloudera          0 2017-11-04 20:31 /user/cloudera/sqoop/test-target-dir-avro-file/_SUCCESS
-rw-r--r--   1 cloudera cloudera      42658 2017-11-04 20:30 /user/cloudera/sqoop/test-target-dir-avro-file/part-m-00000.avro
-rw-r--r--   1 cloudera cloudera      44748 2017-11-04 20:30 /user/cloudera/sqoop/test-target-dir-avro-file/part-m-00001.avro
-rw-r--r--   1 cloudera cloudera      43151 2017-11-04 20:31 /user/cloudera/sqoop/test-target-dir-avro-file/part-m-00002.avro
-rw-r--r--   1 cloudera cloudera      47535 2017-11-04 20:31 /user/cloudera/sqoop/test-target-dir-avro-file/part-m-00003.avro
```
