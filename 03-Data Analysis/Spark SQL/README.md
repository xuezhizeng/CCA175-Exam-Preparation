# Spark SQL
Documentación Spark <br >
https://spark.apache.org/docs/1.6.0/sql-programming-guide.html <br >
https://spark.apache.org/docs/1.6.0/api/python/pyspark.sql.html#pyspark.sql.DataFrame <br >

Documentación Cloudera <br >
https://www.cloudera.com/documentation/enterprise/5-10-x/topics/spark_sparksql.html#spark_sql


## SQLContext and HiveContext
https://www.cloudera.com/documentation/enterprise/5-10-x/topics/spark_sparksql.html#sparksql_sqlcontext

The entry point to all Spark SQL functionality is the SQLContext class or one of its descendants. You create a SQLContext from a SparkContext. With an SQLContext, you can create a DataFrame from an RDD, a Hive table, or a data source.

To work with data stored in Hive or Impala tables from Spark applications, construct a HiveContext, which inherits from SQLContext. With a HiveContext, you can access Hive or Impala tables represented in the metastore database.


## Example
```Python
from pyspark import SparkContext, SparkConf, HiveContext

if __name__ == "__main__":

  # create Spark context with Spark configuration
  conf = SparkConf().setAppName("Data Frame Join")
  sc = SparkContext(conf=conf)
  
  sqlContext = HiveContext(sc)
  
  df_07 = sqlContext.sql("SELECT * from sample_07")
  df_07.filter(df_07.salary > 150000).show()
  
  df_08 = sqlContext.sql("SELECT * from sample_08")
  tbls = sqlContext.sql("show tables")
  tbls.show()
  
  df_09 = df_07.join(df_08, df_07.code == df_08.code).select(df_07.code,df_07.description)
  df_09.show()
  
  df_09.write.saveAsTable("sample_09")
  
  tbls = sqlContext.sql("show tables")
  tbls.show()
```
