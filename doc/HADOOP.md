# Hadoop cheat-sheet

- Executing command a hadopp: `hadoop fs -[command]`

## Files operations

- Upload: `hadoop fs -put ~/file.txt /tmp/file.txt`
- Upload with custom replication factor: `hadoop fs -D dfs.replication=2 -put ~/file.txt /tmp/file.txt`
- Upload with custom file block size (minimal 1048576 and multiples of 512): `hadoop fs -D dfs.block.size=1048576 -put ~/file.txt /tmp/file.txt`
- List files: `hadoop fs -ls /tmp`
- Check file blocks information: `hdfs fsck /tmp/file.txt -files -blocks`

## Map/Reduce jobs

- Running map/reduce job:
```bash
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-files mapper.py,reducer.py \
-mapper mapper.py \
-reducer reducer.py \
-input /tmp/input.txt \
-output /tmp/output # output parameter is a folder
```
- Running map/reduce job forcing number of map/reduce internal tasks:
```bash
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-D mapred.reduce.tasks=1 \
-files mapper.py,reducer.py \
-mapper mapper.py \
-reducer reducer.py \
-input /tmp/input.txt \
-output /tmp/output # output parameter is a folder
```
- Download output of a job in local as single file:
```bash
hadoop fs -getmerge <src> <localdst>
```

