>>> rdd = sc.textFile("/user/cloudera/datasets/state-count.tsv")
>>> rdd.collect()
[u'1\t754\tTX\tIAD', u'2\t1000\tTX\tIND', u'3\t1925\tWN\tJAX', u'4\t2121\tIL\tLAS', u'5\t1132\tTX\tBWI']
>>> rdd2 = rdd.map(lambda x: x.split("  "))
>>> rdd2.collect()
[[u'1', u'754', u'TX', u'IAD'], [u'2', u'1000', u'TX', u'IND'], [u'3', u'1925', u'WN', u'JAX'], [u'4', u'2121', u'IL', u'LAS'], [u'5', u'1132', u'TX', u'BWI']]
>>> from pyspark.sql import Row
>>> rdd3 = rdd2.map(lambda x: Row(state=(x[2])))
>>> df2 = sqlContext.createDataFrame(rdd3)
>>> df2.show()
+-----+
|state|
+-----+
|   TX|
|   TX|
|   WN|
|   IL|
|   TX|
+-----+

>>> df2.registerTempTable("states")
>>> sqlContext.sql("select * from states").show()
+-----+
|state|
+-----+
|   TX|
|   TX|
|   WN|
|   IL|
|   TX|
+-----+

>>> df3 = sqlContext.sql("select state, count(*) as count from states group by state")
>>> df3.show()
+-----+-----+                                                                   
|state|count|
+-----+-----+
|   TX|    3|
|   IL|    1|
|   WN|    1|
+-----+-----+

>>> rddFinal = df3.map(lambda x: str(x[0]) + "," + str(x[1]))
>>> rddFinal.collect()
['TX,3', 'IL,1', 'WN,1']                                                        
>>> rddFinal.saveAsTextFile("/user/cloudera/results/test-delimiter/states.csv")>>> rddFinal.saveAsTextFile("/user/cloudera/results/test-delimiter/states.csv")
