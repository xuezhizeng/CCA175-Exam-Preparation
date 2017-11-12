# Fundamentals of quering

## Creating DataFrames
```Python
from pyspark.sql import SQLContext
sqlContext = SQLContext(sc)

df = sqlContext.read.json("/user/cloudera/spark/people.json")
```

## DataFrame operations
```Python
# Displays the content of the DataFrame to stdout
df.show()
```

| age | name |
| ------------- | ------------- | 
| null | Michael |
| 30 | Andy |
| 19 | Justin |

```Python
# Select only the "name" column
df.select("name").show()
```

| name |
| ------------- | 
| Michael |
| Andy |
| Justin |

```Python
# Select everybody, but increment the age by 1
df.select(df['name'], df['age'] + 1).show()
```

| name | (age + 1) |
| ------------- | ------------- | 
| Michael | null |
| Andy | 31 |
| Justin | 20 |

```Python
# Select people older than 21
df.filter(df['age'] > 21).show()
```

| age | name |
| ------------- | ------------- | 
| 30 | Andy |

```Python
# Count people by age
df.groupBy("age").count().show()
```

| age | count |
| ------------- | ------------- | 
| null | 1 |
| 19 | 1 |
| 30 | 1 |

-----

## Running SQL Queries
```Python
from pyspark.sql import SQLContext
sqlContext = SQLContext(sc)
df = sqlContext.sql("SELECT * FROM table")
```

## Run SQL on files directly
```Python
df = sqlContext.sql("SELECT * FROM parquet.'/user/cloudera/spark/users.parquet'")
```

-----

## Generic Load/Save Functions
```Python
df = sqlContext.read.load("examples/src/main/resources/users.parquet")
df.select("name", "favorite_color").write.save("namesAndFavColors.parquet")
```

## Manually Specifying Options
```Python
df = sqlContext.read.load("examples/src/main/resources/people.json", format="json")
df.select("name", "age").write.save("namesAndAges.parquet", format="parquet")
```

-----

## Interoperating with RDDs
```Python
# sc is an existing SparkContext.
from pyspark.sql import SQLContext, Row
sqlContext = SQLContext(sc)

# Load a text file and convert each line to a Row.
lines = sc.textFile("examples/src/main/resources/people.txt")
parts = lines.map(lambda l: l.split(","))
people = parts.map(lambda p: Row(name=p[0], age=int(p[1])))

# Infer the schema, and register the DataFrame as a table.
schemaPeople = sqlContext.createDataFrame(people)
schemaPeople.registerTempTable("people")

# SQL can be run over DataFrames that have been registered as a table.
teenagers = sqlContext.sql("SELECT name FROM people WHERE age >= 13 AND age <= 19")

# The results of SQL queries are RDDs and support all the normal RDD operations.
teenNames = teenagers.map(lambda p: "Name: " + p.name)
for teenName in teenNames.collect():
  print(teenName)
```
