# Rank and Sort


## Dataset
New record added to test the rank function

```Shell
[cloudera@quickstart cca175-spark]$ cat employees_to_rank.json 
{"name":"Michael", "id_dept":1, "salary":3000}
{"name":"Andy", "id_dept":2, "salary":4500}
{"name":"Justin", "id_dept":2, "salary":3500}
{"name":"Jack", "id_dept":1, "salary":3500}
{"name":"Berta", "id_dept":1, "salary":4000}
```

## Result
|   name|rank|
|-------|----|
|Michael|   1|
| Justin|   2|
|   Jack|   2|
|  Berta|   4|
|   Andy|   5|
