# sc is an existing SparkContext.
from pyspark import SparkConf, SparkContext
from pyspark.sql import HiveContext

conf = SparkConf()
sc = SparkContext(conf=conf)

sqlContext = HiveContext(sc)

sqlContext.sql("CREATE TABLE IF NOT EXISTS src (key INT, value STRING)")
sqlContext.sql("LOAD DATA LOCAL INPATH '/user/cloudera/people.txt' INTO TABLE people")

results = sqlContext.sql("FROM people SELECT key, value").collect()
