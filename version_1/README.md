# influxdb 1
Basic how-to-use influxdb 1

Tutorial link:
- https://www.youtube.com/watch?v=Vq4cDIdz_M8&list=PLY_rQVYyU1sBO6FFBp18B2wEFsLOE_m8C

## Install local InfluxDB
Linux:
```
sudo apt-get install influxdb           #server
sudo apt-get install influxdb-client    #client
```
### Start service
```
sudo service influxdb start
```
### UNINSTALL
```
sudo service influxdb stop
sudo apt-get remove --purge influxdb influxdb-client
sudo apt-get autoremove
```
```
sudo service influxdb status
```

## Run shell
```
influx
```


### SHELL COMMANDS
```
show databases
```
```
create database devopsjourney
```
```
use devopsjourney
```
Measurements are similar to SQL tables:
```
show measurements
```
```
insert MyCPU,host=node1 value=10
```
```
select * from MyCPU
```
```
drop measurement MyCPU
```
tags:
- node1
- node2
- node3
```
insert MyCPU,host=node1 value=10
insert MyCPU,host=node2 value=15
insert MyCPU,host=node3 value=20
select * from MyCPU
```
```
show series
```
Filtering:
```
select * from MyCPU where host='node2'
select * from MyCPU where time>=now()-5m
```