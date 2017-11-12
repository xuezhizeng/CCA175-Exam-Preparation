from pyspark import SparkConf, SparkContext
from pyspark.sql import HiveContext

conf = SparkConf()
sc = SparkContext(conf=conf)
sqlContext = HiveContext(sc)

df = sqlContext.read.json("/user/cloudera/spark/employees_to_rank.json")

df.registerTempTable("employees")

sqlContext.sql("SELECT name, RANK() OVER (ORDER BY salary) as rank FROM employees").show()
