Import control arguments:

* --append	Append data to an existing dataset in HDFS
* --as-avrodatafile	Imports data to Avro Data Files
* --as-sequencefile	Imports data to SequenceFiles
* --as-textfile	Imports data as plain text (default)
* --as-parquetfile	Imports data to Parquet Files
* --columns <col,col,col…>	Columns to import from table
* --delete-target-dir	Delete the import target directory if it exists
* -m,--num-mappers <n>	Use n map tasks to import in parallel
* -e,--query <statement>	Import the results of statement.
* --split-by <column-name>	Column of the table used to split work units. Cannot be used with --autoreset-to-one-mapper option.
* --table <table-name>	Table to read
* --target-dir <dir>	HDFS destination dir
* --warehouse-dir <dir>	HDFS parent for table destination
* --where <where clause>	WHERE clause to use during import
* -z,--compress	Enable compression
* --compression-codec <c>	Use Hadoop codec (default gzip)
* --null-string <null-string>	The string to be written for a null value for string columns
* --null-non-string <null-string>	The string to be written for a null value for non-string columns
