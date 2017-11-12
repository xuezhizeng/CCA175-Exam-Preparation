from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext

conf = SparkConf()
sc = SparkContext(conf=conf)

sqlContext = SQLContext(sc)

df = sqlContext.read.json("/user/cloudera/spark/people.json")

df.show()

df.select(df.name).show()

df.select(df['name'],df['age']+1).show()

df.filter(df['age']>21).show()

df.groupBy("age").count().show()
