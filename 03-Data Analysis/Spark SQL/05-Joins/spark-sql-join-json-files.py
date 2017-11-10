from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext

conf = SparkConf()
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)

df = sqlContext.read.json("/user/cloudera/spark/employees.json")

df2 = sqlContext.read.json("/user/cloudera/spark/departments.json")

df.registerTempTable("employees")

df2.registerTempTable("departments")

df3 = sqlContext("SELECT e.name, avg(d.salary) FROM employees e JOIN departments d ON e.id_dept = d.id GROUP BY e.name")
df3.show()
