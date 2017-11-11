## --hive-import creates the table in Hive
```Shell
sqoop import \
--connect jdbc:mysql://quickstart:3306/retail_db \
--username retail_dba \
--password cloudera \
--table orders \
--hive-import
```
