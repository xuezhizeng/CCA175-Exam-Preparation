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

# Ejemplo

```Shell
$ bin/flume-ng agent --conf conf --conf-file example.conf --name a1 -Dflume.root.logger=INFO,console
```
