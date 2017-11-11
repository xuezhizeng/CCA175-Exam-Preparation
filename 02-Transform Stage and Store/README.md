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
* map(func)	
* filter(func)	
* flatMap(func)	
* union(otherDataset)	
* intersection(otherDataset)	
* distinct([numTasks]))	
* reduceByKey(func, [numTasks])	
* sortByKey([ascending], [numTasks])	
* join(otherDataset, [numTasks])	

### Actions
* reduce(func)
* collect()
* count()
* first()
* take(n)
* saveAsTextFile(path)
* foreach(func)	
