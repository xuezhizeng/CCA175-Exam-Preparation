# Write a file with Compression Codec Snappy

https://www.cloudera.com/documentation/enterprise/5-8-x/topics/introduction_compression_snappy.html
https://www.cloudera.com/documentation/enterprise/5-9-x/topics/introduction_compression.html

```Python
from pyspark import SparkConf, SparkContext
from pyspark.sql import HiveContext

conf = SparkConf()
sc = SparkContext(conf=conf)
sqlContext = HiveContext(sc)

df = sqlContext.sql("SELECT name, age FROM people")

sqlContext.setConf("spark.sql.parquet.compression.codec","snappy")

df.write.parquet("/user/cloudera/spark/people-table-parquet")
```
