from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext

conf = SparkConf()
sc = SparkContext(conf=conf)

sqlContext = SQLContext(sc)

df = sqlContext.read.json("/user/cloudera/people.json")
df.show()

df.printSchema()
# root
#  |-- age: integer (nullable = true)
#  |-- name: string (nullable = true)

df.registerTempTable("people")

df2 = sqlContext.sql("SELECT name FROM people WHERE age BETWEEN 13 AND 19")
df2.show()
