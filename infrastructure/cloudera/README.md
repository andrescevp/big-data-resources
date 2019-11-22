```
docker-composer up --build
```

Install manager: https://docs.cloudera.com/documentation/enterprise/5-5-x/topics/cm_qs_quick_start.html

Windows errors binding ports:

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