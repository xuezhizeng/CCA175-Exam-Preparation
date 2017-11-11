--warehouse-dir creates a new directory named like the table that will be imported in the specified path.

## Step 1
```Shell
sqoop import \
--connect jdbc:mysql://quickstart:3306/retail_db \
--username retail_dba \
--password cloudera \
--table products \
--warehouse-dir /user/cloudera/sqoop/test-con-warehouse-dir
```

## Step 2
```Shell
[cloudera@quickstart ~]$ hdfs dfs -ls /user/cloudera/sqoop/test-con-warehouse-dir/products
Found 5 items
-rw-r--r--   1 cloudera cloudera          0 2017-11-04 18:23 /user/cloudera/sqoop/test-con-warehouse-dir/products/_SUCCESS
-rw-r--r--   1 cloudera cloudera      41419 2017-11-04 18:23 /user/cloudera/sqoop/test-con-warehouse-dir/products/part-m-00000
-rw-r--r--   1 cloudera cloudera      43660 2017-11-04 18:23 /user/cloudera/sqoop/test-con-warehouse-dir/products/part-m-00001
-rw-r--r--   1 cloudera cloudera      42195 2017-11-04 18:23 /user/cloudera/sqoop/test-con-warehouse-dir/products/part-m-00002
-rw-r--r--   1 cloudera cloudera      46719 2017-11-04 18:23 /user/cloudera/sqoop/test-con-warehouse-dir/products/part-m-00003
```

## Step 3
```Shell
[cloudera@quickstart ~]$ hdfs dfs -tail /user/cloudera/sqoop/test-con-warehouse-dir/products/part-m-00000
men's Essential Banded Tank To,,49.99,http://images.acmesports.sports/Under+Armour+Women%27s+Essential+Banded+Tank+Top
330,15,Nike Women's Dri-FIT Cotton Tight Capris,,40.0,http://images.acmesports.sports/Nike+Women%27s+Dri-FIT+Cotton+Tight+Capris
331,15,The North Face Women's Be Calm Tank Top,,38.0,http://images.acmesports.sports/The+North+Face+Women%27s+Be+Calm+Tank+Top
332,15,Under Armour Women's Pure Stretch Sheer Cheek,,12.0,http://images.acmesports.sports/Under+Armour+Women%27s+Pure+Stretch+Sheer+Cheeky+Underwear
333,15,lucy Women's Heart Center Tank Top,,55.0,http://images.acmesports.sports/lucy+Women%27s+Heart+Center+Tank+Top
334,15,Reebok Women's Fitness Essentials Regular Fit,,38.0,http://images.acmesports.sports/Reebok+Women%27s+Fitness+Essentials+Regular+Fit+Pant
335,15,Nike Women's Dri-FIT Cotton Regular-Fit Capri,,45.0,http://images.acmesports.sports/Nike+Women%27s+Dri-FIT+Cotton+Regular-Fit+Capris
336,15,Nike Swoosh Headband - 2",,5.0,http://images.acmesports.sports/Nike+Swoosh+Headband+-+2%22
```
