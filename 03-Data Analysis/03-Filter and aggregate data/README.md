# Filter (condition)
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

```Python
# To create DataFrame using SQLContext
people = sqlContext.read.parquet("...")
department = sqlContext.read.parquet("...")

people.filter(people.age > 30). \
  join(department, people.deptId == department.id)). \
  groupBy(department.name, "gender"). \
  agg({"salary": "avg", "age": "max"})
```
