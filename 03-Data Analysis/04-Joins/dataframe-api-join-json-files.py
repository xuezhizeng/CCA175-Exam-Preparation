from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext

conf = SparkConf()
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)

df = sqlContext.read.json("/user/cloudera/spark/employees_by_dept.json")

df2 = sqlContext.read.json("/user/cloudera/spark/departments.json")

df.show()

df2.show()

df.join(df2,df.id_dept==df2.id). \
        select(df2.name, df.salary). \
        groupBy(df2.name). \
        avg('salary'). \
        show()
