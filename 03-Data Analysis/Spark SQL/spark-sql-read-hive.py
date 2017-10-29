from pyspark import SparkConf, SparkContext
from pyspark.sql import HiveContext, Row

conf = SparkConf()
sc = SparkContext(conf=conf)

sqlContext = HiveContext(sc)

rdd = sc.textFile("/user/cloudera/people.txt")

rdd2 = rdd.map(lambda x: x.split(","))
rdd3 = rdd2.map(lambda x: Row(name=(x[0]),age=int(x[1])))

df = sqlContext.createDataFrame(rdd3)
df.registerTempTable("people_temp")

sqlContext.sql("DROP TABLE people")
sqlContext.sql("CREATE TABLE IF NOT EXISTS people (name STRING, age INT)")
sqlContext.sql("INSERT INTO people SELECT name, age FROM people_temp")

df2 = sqlContext.sql("SELECT * FROM people").show()
