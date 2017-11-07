# Preparing the environment

## Import all tables from retail_db using Sqoop
```Shell
sqoop import-all-tables \
--connect jdbc:mysql://quickstart:3306/retail_db \
--username retail_dba \
--password cloudera \
--hive-import
```

## Hive warehouse
```Shell
[cloudera@quickstart ~]$ hdfs dfs -ls /user/hive/warehouse
Found 6 items
drwxrwxrwx   - cloudera supergroup          0 2017-11-07 15:11 /user/hive/warehouse/categories
drwxrwxrwx   - cloudera supergroup          0 2017-11-07 15:12 /user/hive/warehouse/customers
drwxrwxrwx   - cloudera supergroup          0 2017-11-07 15:12 /user/hive/warehouse/departments
drwxrwxrwx   - cloudera supergroup          0 2017-11-07 15:13 /user/hive/warehouse/order_items
drwxrwxrwx   - cloudera supergroup          0 2017-11-07 15:14 /user/hive/warehouse/orders
drwxrwxrwx   - cloudera supergroup          0 2017-11-07 15:15 /user/hive/warehouse/products
```
