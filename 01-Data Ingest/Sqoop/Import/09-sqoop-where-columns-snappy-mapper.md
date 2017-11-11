## Parameters 
- where: filter the table to import
- columns: select the columns to import
- compression-codec: select compression-codec (in this case Snappy)
- mappers: number of mappers (in this case 1, default 4)

```Shell
sqoop import \
--connect jdbc:mysql://quickstart:3306/retail_db \
--username retail_dba \
--password cloudera \
--table products \
--columns "product_name, product_price" \
--where "product_price > 30.00" \
--delete-target-dir \
--compression-codec snappy \
-m 1
```

## With Snappy
```Shell
[cloudera@quickstart ~]$ hdfs dfs -ls /user/cloudera/products
Found 2 items
-rw-r--r--   1 cloudera cloudera          0 2017-11-04 21:09 /user/cloudera/products/_SUCCESS
-rw-r--r--   1 cloudera cloudera      15419 2017-11-04 21:09 /user/cloudera/products/part-m-00000.snappy
```

## Without Snappy
```Shell
[cloudera@quickstart ~]$ hdfs dfs -ls /user/cloudera/products
Found 2 items
-rw-r--r--   1 cloudera cloudera          0 2017-11-04 21:06 /user/cloudera/products/_SUCCESS
-rw-r--r--   1 cloudera cloudera      45985 2017-11-04 21:06 /user/cloudera/products/part-m-00000
```
