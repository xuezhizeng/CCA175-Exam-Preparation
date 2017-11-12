from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext

conf = SparkConf()
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)

df = sqlContext.read.json("/user/cloudera/spark/employees_by_dept.json")

df2 = sqlContext.read.json("/user/cloudera/spark/departments.json")

df.registerTempTable("employees")

df2.registerTempTable("departments")

df3 = sqlContext.sql(" \
        SELECT d.name, AVG(e.salary) AS prom_salary \
        FROM employees e \
        JOIN departments d ON e.id_dept = d.id \
        GROUP BY d.name")

df3.show()
