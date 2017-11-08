from pyspark import SparkConf, SparkContext
from pyspark.sql import HiveContext

conf = SparkConf()
sc = SparkContext(conf=conf)
sqlContext = HiveContext(sc)

sqlContext.sql("DROP TABLE people")
sqlContext.sql("CREATE TABLE IF NOT EXISTS people (name STRING, age INT)")

# $ ~/people.txt
sqlContext.sql("LOAD DATA LOCAL INPATH 'people.txt' INTO TABLE people")

results = sqlContext.sql("SELECT name, age FROM people")

results.show()
