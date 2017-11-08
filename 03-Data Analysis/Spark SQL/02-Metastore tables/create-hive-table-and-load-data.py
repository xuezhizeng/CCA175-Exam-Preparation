from pyspark import SparkConf, SparkContext
from pyspark.sql import HiveContext, Row

conf = SparkConf()
sc = SparkContext(conf=conf)
sqlContext = HiveContext(sc)

sqlContext.sql("DROP TABLE people")
sqlContext.sql("CREATE TABLE IF NOT EXISTS people(name STRING, age INT) ROW FORMAT DELIMITED FIELDS TERMINATED BY \",\"")

rdd = sc.textFile("/user/cloudera/spark/people.txt") \
        .map(lambda x: x.split(",")) \
        .map(lambda x: Row( name=x[0], age=int(x[1]) ))

df = sqlContext.createDataFrame(rdd)
df.select(df.name,df.age).write.insertInto("people")

df2 = sqlContext.sql("select * from people").show()
