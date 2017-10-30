# FLUME

https://flume.apache.org/FlumeUserGuide.html


```Shell
[cloudera@quickstart ~]$ flume-ng help
Usage: /usr/lib/flume-ng/bin/flume-ng <command> [options]...

commands:
  help                      display this help text
  agent                     run a Flume agent

global options:
  --conf,-c <conf>          use configs in <conf> directory

agent options:
  --name,-n <name>          the name of this agent (required)
  --conf-file,-f <file>     specify a config file (required if -z missing)

```

## Sources
* Avro Source
* Thrift Source
* Exec Source
* Spooling Directory Source
* NetCat Source
* Sequence Generator Source
* Syslog Sources
* Syslog TCP Source
* Syslog UDP Source
* HTTP Source

## Channels
* Memory Channel
* File Channel

## Sinks
* HDFS Sink

## Examples
https://www.cloudera.com/documentation/other/tutorial/CDH5/topics/ht_flume_to_hdfs.html <br >
https://www.tutorialspoint.com/apache_flume/apache_flume_quick_guide.htm <br >
http://www.bogotobogo.com/Hadoop/BigData_hadoop_CDH5_Flume_Introduction.php
