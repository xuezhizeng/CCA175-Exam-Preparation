from pyspark import SparkConf, SparkContext
from pyspark.sql import HiveContext

conf = SparkConf()
sc = SparkContext(conf=conf)
sqlContext = HiveContext(sc)

df = sqlContext.read.json("/user/cloudera/spark/people.json")

df.write.format('com.databricks.spark.avro').save("/user/cloudera/spark/people-table-avro")
