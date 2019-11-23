Getting started
===
```
docker-composer up --build
```

Cloudera manager
---
```
docker exec -ti cloudera_quickstart bash

# ./home/cloudera/cloudera-manager --express
```



Recommendations
---

Increase the dockers CPU to 4 and memory to 8GB and swap to 2048 


Windows errors binding ports:
---
Show ports 
```
netsh interface ipv4 show excludedportrange protocol=tcp
```
fix: https://github.com/docker/for-win/issues/3171#issuecomment-459205576

Normal ports to open:


Exclude port
```
dism.exe /Online /Disable-Feature:Microsoft-Hyper-V

netsh int ipv4 add excludedportrange protocol=tcp startport={port} numberofports=1

dism.exe /Online /Enable-Feature:Microsoft-Hyper-V /All
```