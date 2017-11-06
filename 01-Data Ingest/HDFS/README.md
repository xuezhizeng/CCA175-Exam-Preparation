# HDFS

https://hadoop.apache.org/docs/r2.7.1/hadoop-project-dist/hadoop-common/FileSystemShell.html

## Show the content of a file loaded in HDFS
```Shell
$ hdfs dfs -tail /user/cloudera/file1
$ hdfs dfs -head /user/cloudera/file1
$ hdfs dfs -cat /user/cloudera/file1
```

## Upload files or directories into HDFS
```Shell
$ hdfs dfs -put file1 /user/cloudera/file1
$ hdfs dfs -copyFromLocal file1 /user/cloudera/file1
```

## Download files or directories from HDFS
```Shell
$ hdfs dfs -get /user/cloudera/file1 file1
$ hdfs dfs -copyToLocal /user/cloudera/file1 file1
```

## List the content of a directory in HDFS
```Shell
$ hdfs dfs -ls /user/cloudera
```

## Create a directory in HDFS
```Shell
$ hdfs dfs -mkdir /user/cloudera/test-mkdir
```

## Delete a file or directory in HDFS
```Shell
$ hdfs dfs -rm /user/cloudera/file1
$ hdfs dfs -rm -r /user/cloudera/test-mkdir
```
