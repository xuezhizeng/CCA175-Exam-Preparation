from pyspark import SparkConf, SparkContext
from pyspark.sql import HiveContext

conf = SparkConf()
sc = SparkContext(conf=conf)
sqlContext = HiveContext(sc)

df = sqlContext.read.format('com.databricks.spark.avro').load("/user/cloudera/spark/users.avro")

df.write.json("/user/cloudera/spark/users.json")
