Dictionaries
---

http://www.ilovelanguages.com/IDP/files/German.txt
http://www.ilovelanguages.com/IDP/files/French.txt
http://www.ilovelanguages.com/IDP/files/Spanish.txt
http://www.ilovelanguages.com/IDP/files/Italian.txt

Running
---

```
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -files mapper.py,reducer.py -mapper mapper.py -reducer reducer.py -input /tmp/dictionary_full.txt -output /tmp/dictionary_full_merged.txt
hadoop fs -cat /tmp/dictionary_full_merged.txt/part-* > /tmp/output.txt
cat /tmp/output.txt | grep house
```