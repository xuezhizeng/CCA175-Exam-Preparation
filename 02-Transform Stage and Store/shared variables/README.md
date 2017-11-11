# Shared variables

## Broadcast variables
```Python
>>> broadcastVar = sc.broadcast([1, 2, 3])

>>> broadcastVar.value
[1, 2, 3]
```

## Accumulators
```Python
>>> accum = sc.accumulator(0)

>>> sc.parallelize([1, 2, 3, 4]).foreach(lambda x: accum.add(x))

>>> accum.value
10
```
### Sample data

Execute a tail 
```Shell
[cloudera@quickstart ~]$ sudo tail /var/log/anaconda.log 
05:56:28,299 DEBUG   : writeksconfig is a direct step
05:56:28,299 INFO    : Writing autokickstart file
05:56:28,317 INFO    : leaving (1) step writeksconfig
05:56:28,318 INFO    : moving (1) to step setfilecon
05:56:28,318 DEBUG   : setfilecon is a direct step
05:56:28,318 INFO    : setting SELinux contexts for anaconda created files
05:56:30,557 INFO    : leaving (1) step setfilecon
05:56:30,558 INFO    : moving (1) to step copylogs
05:56:30,558 DEBUG   : copylogs is a direct step
05:56:30,558 INFO    : Copying anaconda logs
```

Save the output as a file
```Shell
[cloudera@quickstart ~]$ vi logs.txt

[cloudera@quickstart ~]$ hdfs dfs -put logs.txt /user/cloudera/spark/
```
