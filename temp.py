#Best File 2016.
from w1thermsensor import W1ThermSensor
import os
import time
from influxdb import InfluxDBClient

while True:
        sensor1 = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, "041601403dff") #first temp sensor
        sensor1_val = sensor1.get_temperature()
	print(sensor1_val)

        sensor2 = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, "0316054850ff") #second one
	sensor2_val = sensor2.get_temperature()
	print(sensor2_val)

	time.sleep(2)

