# Troubleshooting

## Cloudera

### HDFS

```shell script
sudo  service hadoop-hdfs-namenode restart # conection errors

sudo  service hadoop-hdfs-datanode restart # connection errors, 0 data nodes

sudo -u hdfs hdfs dfsadmin -safemode leave # if security error

sudo service hadoop-yarn-resourcemanager restart # if retry loop
```

## knime

If you get errors running Knime docker, make sure you give permissions to the folders:

- docker/knime/.eclipse
- docker/knime/workspace