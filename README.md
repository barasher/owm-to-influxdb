# OperWeatherMap to InfluxDB (owm-to-influxdb)

**OpenWeatherMap to InfluxDB** is a Docker image that stores a [OpenWeatherMap](https://openweathermap.org/) station temperature to [InfluxDB](https://docs.influxdata.com/influxdb/).

## Image building
 
```
docker build -t barasher/owm-to-influxdb:latest .
```

## Execution

Environment variables :
- **OTI_OWM_APPID**: OpenWeatherMap app id, required
- **OTI_OWM_STATION**: OpenWeatherMap station id, required
- **OTI_IDB_URL**: InfluxDB URL, required (ex : http://192.168.0.2:8086)
- **OTI_IDB_DB**: InfluxDB database, required
- **OTI_IDB_LOC**: Location, required (No space and special character)

Available stations can be retrieved [here](http://bulk.openweathermap.org/sample/city.list.json.gz).

```
docker run --rm
  --env OTI_OWM_APPID=[OpenWeatherMap app id]
  --env OTI_OWM_STATION=[OpenWeatherMap station id]
  --env OTI_IDB_URL=[InfluxDB URL]
  --env OTI_IDB_DB=[InfluxDB database]
  --env OTI_IDB_LOC=[Localisation]
  barasher/owm-to-influxdb:latest
```
