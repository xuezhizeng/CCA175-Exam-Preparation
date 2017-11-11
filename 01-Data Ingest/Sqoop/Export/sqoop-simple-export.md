## Create a table in MySQL
```MySQL
-- Copy the structure of the products table.
CREATE TABLE products_for_export AS SELECT * FROM products WHERE 1 = 2;
```

## Export data from HDFS
```Shell
$ sqoop export \
--connect jdbc:mysql://quickstart:3306/retail_db \
--username retail_dba \
--password cloudera \
--table products_for_export \
--export-dir /user/cloudera/products
```
