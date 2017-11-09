from pyspark import SparkConf, SparkContext
from pyspark.sql import HiveContext

conf = SparkConf()
sc = SparkContext(conf=conf)
sqlContext = HiveContext(sc)

df = sqlContext.sql("SELECT name, age FROM people")

df.write.format('com.databricks.spark.avro').save("/user/cloudera/spark/people-table-avro")
