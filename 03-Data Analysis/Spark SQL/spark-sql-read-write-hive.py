from pyspark import SparkConf, SparkContext
from pyspark.sql import HiveContext, Row

conf = SparkConf()
sc = SparkContext(conf=conf)

sqlContext = HiveContext(sc)

rdd = sc.textFile("/user/cloudera/people.txt") \
        .map(lambda x: x.split(",")) \
        .map(lambda x: Row(name=(x[0]),age=int(x[1])))

df = sqlContext.createDataFrame(rdd)

df.write.saveAsTable("people",mode="overwrite")

sqlContext.sql("SELECT name,age FROM people").show()
