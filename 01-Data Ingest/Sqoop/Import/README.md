
# sqoop import --help
```Shell
[cloudera@quickstart ~]$ sqoop import --help
usage: sqoop import [GENERIC-ARGS] [TOOL-ARGS]

Common arguments:
   --connect <jdbc-uri>                                       Specify JDBC connect string
   --username <username>                                      Set authentication username
   --password <password>                                      Set authentication password

Import control arguments:
   --append                                                   Imports data in append mode
   --as-avrodatafile                                          Imports data to Avro data files
   --as-parquetfile                                           Imports data to Parquet files
   --as-textfile                                              Imports data as plain text (default)
   --columns <col,col,col...>                                 Columns to import from table
   --compression-codec <codec>                                Compression codec to use for import
   --delete-target-dir                                        Imports data in delete mode
   -e,--query <statement>                                     Import results of SQL 'statement'
   -m,--num-mappers <n>                                       Use 'n' map tasks to import in parallel
   --split-by <column-name>                                   Column of the table used to split work units
   --table <table-name>                                       Table to read
   --target-dir <dir>                                         HDFS plain table destination
   --warehouse-dir <dir>                                      HDFS parent for table destination
   --where <where clause>                                     WHERE clause to use during import
   -z,--compress                                              Enable compression

Output line formatting arguments:
   --enclosed-by <char>               Sets a required field enclosing character
   --escaped-by <char>                Sets the escape character
   --fields-terminated-by <char>      Sets the field separator character
   --lines-terminated-by <char>       Sets the end-of-line character


```
