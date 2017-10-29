# Spark Core

Documentación Spark <br >

https://spark.apache.org/docs/1.6.0/programming-guide.html <br >

Documentación Cloudera <br >

https://www.cloudera.com/documentation/enterprise/5-10-x/topics/spark_develop_run.html <br >

## Linking and Initializing
```Python
from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName(appName).setMaster(master)
sc = SparkContext(conf=conf)
```

## Resilient Distributed Datasets (RDDs)

### Parallelized Collections
```Python
data = [1, 2, 3, 4, 5]
distData = sc.parallelize(data)
```

### External Datasets
```Python
distFile = sc.textFile("data.txt")
```

### RDD Operations
```Python
lines = sc.textFile("data.txt")
lineLengths = lines.map(lambda s: len(s))
totalLength = lineLengths.reduce(lambda a, b: a + b)
```

### Transformations

map(func)	
Return a new distributed dataset formed by passing each element of the source through a function func.

filter(func)	
Return a new dataset formed by selecting those elements of the source on which func returns true.

flatMap(func)	
Similar to map, but each input item can be mapped to 0 or more output items (so func should return a Seq rather than a single item).

union(otherDataset)	
Return a new dataset that contains the union of the elements in the source dataset and the argument.

intersection(otherDataset)	
Return a new RDD that contains the intersection of elements in the source dataset and the argument.

distinct([numTasks]))	
Return a new dataset that contains the distinct elements of the source dataset.

reduceByKey(func, [numTasks])	
When called on a dataset of (K, V) pairs, returns a dataset of (K, V) pairs where the values for each key are aggregated using the given reduce function func, which must be of type (V,V) => V. Like in groupByKey, the number of reduce tasks is configurable through an optional second argument.

sortByKey([ascending], [numTasks])	
When called on a dataset of (K, V) pairs where K implements Ordered, returns a dataset of (K, V) pairs sorted by keys in ascending or descending order, as specified in the boolean ascending argument.

join(otherDataset, [numTasks])	
When called on datasets of type (K, V) and (K, W), returns a dataset of (K, (V, W)) pairs with all pairs of elements for each key. Outer joins are supported through leftOuterJoin, rightOuterJoin, and fullOuterJoin.
