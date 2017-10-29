# FLUME

https://flume.apache.org/FlumeUserGuide.html

* Sources: recibe datos y los envia a los channels.
* Channels: sirven como conductos entre los sources y los sinks
* Sinks: procesa los datos que fueron tomados desde los channels y los entrega al destino.

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
