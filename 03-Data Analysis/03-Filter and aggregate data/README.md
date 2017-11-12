## Filter (condition)
Filters rows using the given condition.

where() is an alias for filter().

Parameters:	condition – a Column of types.BooleanType or a string of SQL expression.
```Python
>>> df.filter(df.age > 3).collect()
[Row(age=5, name=u'Bob')]

>>> df.where(df.age == 2).collect()
[Row(age=2, name=u'Alice')]
```

```Python
>>> df.filter("age > 3").collect()
[Row(age=5, name=u'Bob')]

>>> df.where("age = 2").collect()
[Row(age=2, name=u'Alice')]
```

## Aggregate 
agg(*exprs)
Compute aggregates and returns the result as a DataFrame.

The available aggregate functions are avg, max, min, sum, count.

Parameters:	exprs – a dict mapping from column name (string) to aggregate functions (string), or a list of Column.

```Python
>>> gdf = df.groupBy(df.name)
>>> gdf.agg({"*": "count"}).collect()
[Row(name=u'Alice', count(1)=1), Row(name=u'Bob', count(1)=1)]

>>> df.groupBy('name').agg({'age': 'mean'}).collect()
[Row(name=u'Alice', avg(age)=2.0), Row(name=u'Bob', avg(age)=5.0)]

>>> df.groupBy(df.name).avg().collect()
[Row(name=u'Alice', avg(age)=2.0), Row(name=u'Bob', avg(age)=5.0)]

>>> df.groupBy(['name', df.age]).count().collect()
[Row(name=u'Bob', age=5, count=1), Row(name=u'Alice', age=2, count=1)]
```

## Filter and Aggregate
```Python
# To create DataFrame using SQLContext
people = sqlContext.read.parquet("...")
department = sqlContext.read.parquet("...")

people.filter(people.age > 30). \
  join(department, people.deptId == department.id)). \
  groupBy(department.name, "gender"). \
  agg({"salary": "avg", "age": "max"})
```
