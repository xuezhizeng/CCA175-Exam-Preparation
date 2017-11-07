# Metastore tables

## SQLContext and HiveContext
https://www.cloudera.com/documentation/enterprise/5-10-x/topics/spark_sparksql.html#sparksql_sqlcontext

The entry point to all Spark SQL functionality is the SQLContext class or one of its descendants. You create a SQLContext from a SparkContext. With an SQLContext, you can create a DataFrame from an RDD, a Hive table, or a data source.

To work with data stored in Hive or Impala tables from Spark applications, construct a HiveContext, which inherits from SQLContext. With a HiveContext, you can access Hive or Impala tables represented in the metastore database.


## Preparing the environment
### Import all tables from retail_db using Sqoop
```Shell
sqoop import-all-tables \
--connect jdbc:mysql://quickstart:3306/retail_db \
--username retail_dba \
--password cloudera \
--hive-import
```
