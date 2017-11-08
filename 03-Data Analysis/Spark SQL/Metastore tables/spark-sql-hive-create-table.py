from pyspark import SparkConf, SparkContext
from pyspark.sql import HiveContext, Row

conf = SparkConf()
sc = SparkContext(conf=conf)
sqlContext = HiveContext(sc)

sqlContext.sql("CREATE TABLE IF NOT EXISTS people(name STRING, age INT)")

rdd = sc.textFile("/user/cloudera/spark/people.txt").map(lambda x: x.split(",")).map(lambda x: Row( name=x[0], age=x[1] ))

df = sqlContext.createDataFrame(rdd)

df.show()


