from pyspark import SparkConf, SparkContext

conf = SparkConf()
sc = SparkContext(conf=conf)

rdd = sc.textFile("/user/cloudera/spark/logs.txt"). \
  map(lambda x: x.split(" ")). \
  map(lambda x: x[1]). \
  filter(lambda x: x == "DEBUG")

print rdd.collect()

accum = sc.accumulator(0)

rdd.foreach(lambda x: accum.add(1))

print accum.value
