## Import all tables from retail_db using Sqoop
```Shell
sqoop import-all-tables \
--connect jdbc:mysql://quickstart:3306/retail_db \
--username retail_dba \
--password cloudera \
--hive-import \
--as-textfile \
--fields-terminated-by "," 
```

## Hive warehouse
```Shell
[cloudera@quickstart ~]$ hdfs dfs -ls /user/hive/warehouse/Found 6 items
drwxrwxrwx   - cloudera supergroup          0 2017-11-07 15:41 /user/hive/warehouse/categories
drwxrwxrwx   - cloudera supergroup          0 2017-11-07 15:41 /user/hive/warehouse/customers
drwxrwxrwx   - cloudera supergroup          0 2017-11-07 15:42 /user/hive/warehouse/departments
drwxrwxrwx   - cloudera supergroup          0 2017-11-07 15:43 /user/hive/warehouse/order_items
drwxrwxrwx   - cloudera supergroup          0 2017-11-07 15:44 /user/hive/warehouse/orders
drwxrwxrwx   - cloudera supergroup          0 2017-11-07 15:44 /user/hive/warehouse/products
```

## Checking the output
```Shell
[cloudera@quickstart ~]$ hdfs dfs -tail /user/hive/warehouse/customers/part-m-00000
Lynn,MA,01902
3097,Douglas,Hanna,XXXXXXXXX,XXXXXXXXX,1112 Rustic Range,Caguas,PR,00725
3098,Mary,Smith,XXXXXXXXX,XXXXXXXXX,8217 Fallen Panda Walk,Newburgh,NY,12550
3099,Brittany,Copeland,XXXXXXXXX,XXXXXXXXX,5735 Round Beacon Terrace,Caguas,PR,00725
3100,Mary,Smith,XXXXXXXXX,XXXXXXXXX,5436 Grand Hickory Farm,Huntington Park,CA,90255
3101,George,Reyes,XXXXXXXXX,XXXXXXXXX,8702 Silver Apple Square,Mission Viejo,CA,92692
3102,Ralph,Dixon,XXXXXXXXX,XXXXXXXXX,5633 Harvest Turnabout,Caguas,PR,00725
3103,Mary,Wilkins,XXXXXXXXX,XXXXXXXXX,1213 Cotton Pike,Spring Valley,NY,10977
3104,Megan,Smith,XXXXXXXXX,XXXXXXXXX,5292 Shady Pony Cape,Caguas,PR,00725
3105,Mary,Stone,XXXXXXXXX,XXXXXXXXX,8510 Green River Acres,Toa Baja,PR,00949
3106,Samantha,Smith,XXXXXXXXX,XXXXXXXXX,355 Cozy Square,Las Cruces,NM,88005
3107,Tiffany,Estes,XXXXXXXXX,XXXXXXXXX,5182 Cotton Heath,Caguas,PR,00725
3108,Mary,Smith,XXXXXXXXX,XXXXXXXXX,577 Rustic Nectar Row,Houston,TX,77083
3109,Jack,James,XXXXXXXXX,XXXXXXXXX,5876 Burning Mall ,Fort Worth,TX,76133
```

