Troubleshooting
===

max virtual memory areas vm.max_map_count [65530] is too low, increase to at least [262144]
---
Windows/Mac

You can setup in the docker manager UI

In linux:

```
sysctl -w vm.max_map_count=262144
```