# Flume

To avoid errors with log4j add the following argument to the command

-Dlog4j.configuration=file:conf/log4j.properties

## Running examples

```shell script
bin/flume-ng agent --conf-file conf/examples/console_io.conf.properties --name a1 -Dflume.root.logger=INFO,console
bin/flume-ng agent --conf-file conf/examples/console_io_to_hdfs.conf.properties --name a1 -Dflume.root.logger=INFO,console
bin/flume-ng agent --conf-file conf/examples/twitter_to_hdfs.conf.properties --name a1 -Dflume.root.logger=INFO,console # need edit the config file to add twitter credentials
```