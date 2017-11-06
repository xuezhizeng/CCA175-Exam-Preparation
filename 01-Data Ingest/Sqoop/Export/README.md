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
   
Input parsing arguments:
   --input-enclosed-by <char>               Sets a required field encloser
   --input-escaped-by <char>                Sets the input escape character
   --input-fields-terminated-by <char>      Sets the input field separator
   --input-lines-terminated-by <char>       Sets the input end-of-line char
   --input-optionally-enclosed-by <char>    Sets a field enclosing character

Output line formatting arguments:
   --enclosed-by <char>               Sets a required field enclosing character
   --escaped-by <char>                Sets the escape character
   --fields-terminated-by <char>      Sets the field separator character
   --lines-terminated-by <char>       Sets the end-of-line character

Code generation arguments:
   --input-null-non-string <null-str>         Input null non-string representation
   --input-null-string <null-str>             Input null string representation types
   --null-non-string <null-str>               Null non-string representation
   --null-string <null-str>                   Null string representation

At minimum, you must specify --connect, --export-dir, and --table
```
