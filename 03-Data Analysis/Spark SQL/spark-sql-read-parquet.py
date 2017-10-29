from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext

conf = SparkConf()
sc = SparkContext(conf=conf)

sqlContext = SQLContext(sc)

users = sqlContext.read.parquet("/user/cloudera/users.parquet")
users.show()
