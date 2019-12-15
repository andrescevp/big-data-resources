# Summary

The point is import data with mysql and sqoop.

Use the cloudera docker.

## Checking mysql

```shell script
mysql -u root -p

#in mysql console

show databases; #get databases list
exit # go out of mysql console

# out of mysql console

sqoop import --connect jdbc:mysql://localhost/retail_db --username root --password cloudera --table customers --target-dir /tmp/exportDB/ -m 1
```

## Import
```shell script
sqoop import --connect jdbc:mysql://localhost/mysql --username root --password cloudera --table user --target-dir /tmp/exportDB/ -m 1
```