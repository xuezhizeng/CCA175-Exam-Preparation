## sqoop export --help
```Shell
[cloudera@quickstart ~]$ sqoop export --help
usage: sqoop export [GENERIC-ARGS] [TOOL-ARGS]

Common arguments:
   --connect <jdbc-uri>                                       Specify JDBC connect string
   --help                                                     Print usage instructions
   --password <password>                                      Set authentication password
   --username <username>                                      Set authentication username

Export control arguments:
   --columns <col,col,col...>                                 Columns to export to table
   --direct                                                   Use direct export fast path
   --export-dir <dir>                                         HDFS source path for the export
   -m,--num-mappers <n>                                       Use 'n' map tasks to export in parallel
   --table <table-name>                                       Table to populate

At minimum, you must specify --connect, --export-dir, and --table
```
