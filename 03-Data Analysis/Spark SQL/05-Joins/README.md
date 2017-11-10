# Joins
Example: join to json files

## employees.json
```Shell
[cloudera@quickstart cca175-spark]$ hdfs dfs -cat /user/cloudera/spark/employees.json
{"name":"Michael", "id_dept":1, "salary":3000}
{"name":"Andy", "id_dept":2, "salary":4500}
{"name":"Justin", "id_dept":2, "salary":3500}
{"name":"Berta", "id_dept":1, "salary":4000}
```

## departments.json
```Shell
[cloudera@quickstart cca175-spark]$ hdfs dfs -cat /user/cloudera/spark/departments.json
{"id":1, "name":"HR"}
{"id":2, "name":"IT"}
```
