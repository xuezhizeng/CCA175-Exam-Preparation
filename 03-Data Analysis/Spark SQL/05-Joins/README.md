# Joins
Example: join to json files

## employees.json
```Shell
[cloudera@quickstart cca175-spark]$ hdfs dfs -cat /user/cloudera/spark/employees.json
{"name":"Michael", "salary":3000}
{"name":"Andy", "salary":4500}
{"name":"Justin", "salary":3500}
{"name":"Berta", "salary":4000}
```

## departments.json
```Shell
[cloudera@quickstart cca175-spark]$ hdfs dfs -cat /user/cloudera/spark/departments.json
{"id":1, "name":"HR"}
{"id":2, "name":"IT"}
```
