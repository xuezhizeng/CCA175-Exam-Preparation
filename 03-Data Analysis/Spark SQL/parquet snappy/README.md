# Write a file with Compression Codec Snappy
```Python
from pyspark import SparkConf, SparkContext
from pyspark.sql import HiveContext

conf = SparkConf()
sc = SparkContext(conf=conf)
sqlContext = HiveContext(sc)

df = sqlContext.sql("SELECT name, age FROM people")

df.show()

sqlContext.setConf("spark.sql.parquet.compression.codec","snappy")

df.map(lambda x: str(x.name)+","+str(x.age)).saveAsTextFile("/user/cloudera/spark/people-table-to-csv")
```
