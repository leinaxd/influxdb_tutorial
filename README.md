# HOW TO: INFLUXDB 2
Basic how-to-use influxdb 2

Docs:
- https://docs.influxdata.com/influxdb/v2/install/
- https://docs.influxdata.com/influxdb/v2/tools/influx-cli/

Insight video:
- https://www.youtube.com/watch?v=W-ouPw944CM

DOCKER:
- https://www.youtube.com/watch?v=-gF-Jsk85bQ

## Install SERVER and CLI (local) InfluxDB
Linux:
- Download key
- Validate
- add key to trusted
- add repository
- update
- install
```
curl --silent --location -O https://repos.influxdata.com/influxdata-archive.key
```
```
echo "943666881a1b8d9b849b74caebf02d3465d6beb716510d86a39f6c8e8dac7515  influxdata-archive.key" | sha256sum --check -
```
```
sudo cat influxdata-archive.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/influxdata-archive.gpg > /dev/null
```
```
echo 'deb [signed-by=/etc/apt/trusted.gpg.d/influxdata-archive.gpg] https://repos.influxdata.com/debian stable main' | sudo tee /etc/apt/sources.list.d/influxdata.list
```
```
sudo apt-get update
sudo apt-get install influxdb2
```

### INSTALL SHELL V2
```
wget https://dl.influxdata.com/influxdb/releases/influxdb2-client-2.3.0-linux-amd64.tar.gz

tar xvzf path/to/influxdb2-client-2.3.0-linux-amd64.tar.gz

sudo cp influxdb2-client-2.3.0-linux-amd64/influx /usr/local/bin/
```
```
influx config create --config-name onboarding \
    --host-url "http://localhost:8086" \
    --org "841d907534a3079f" \
    --token "iZfE1O7hs8ncUuTFPpUXB49Kk51oGtdrnuXf688f62bDm19sEpQMC9rrcwL3srKiXZSigZ52SLHm1MuQKPmc3g==" \
    --active
```
```
influx bucket create --name sample-bucket -c onboarding --org-id 841d907534a3079f
```
Download data 'air-sensor-data-annotated.csv
```
influx write --bucket test --file downloads/air-sensor-data-annotated.csv
```
```
influx query 'from(bucket:"test") |> range(start:-30m)'
```
```
influx query 'from(bucket:"test") |> range(start:-30m) |> mean()'
```
### Start service
```
sudo service influxdb start
sudo service influxdb status
```
```
localhost:8086
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
CREATE BUCKET <my_bucket>
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