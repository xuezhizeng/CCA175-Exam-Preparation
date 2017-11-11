## Import all tables in the retail_db into de default database in Hive
```Shell
$ sqoop import-all-tables \
--connect jdbc:mysql://quickstart:3306/retail_db \
--username retail_dba --password cloudera
```
