# Project control code for JMKWeather Project
# 16JUN2020: Written: JMK

import datetime
import board
import busio
import adafruit_bme280
import WeatherStix

w = WeatherStix()
# (self, datetime, precip, temp, humidity, windspeed, avgwindspeed2m,
#                  winddirection, avgwinddirection2m, windgust, windgustdir, windgust10m,
#                  windgustdir10m, battery, barometer, lightlevel. altitude)
w.datetime = datetime
print(w.datetime)

# Retrieve values from 4 sensors in BME280 device from Adafruit
# using I2C communications

i2c = busio.I2C(board.SCL, board.SDA)
bme280 = adafruit.bme280.Adafruit_BME280_I2C(i2c)
# temperature - The sensor temperature in degrees Celsius
# Tf = (9/5)*Tc+32; Tc = temperature in degrees Celsius, Tf = temperature in degrees Fahrenheit
# So the temperature is (9/5)*40 + 32 = 72 + 32 = 104 degrees Fahrenheit
# humidity - The percent humidity as a value from 0% - 100%
# pressure - The pressure in hPa
# altitude - The altitude in meters

# print("\nTemperature: %0.1f C" % bme280.temperature)
# print("Humidity: %0.1f %%" % bme280.humidity)
# print("Pressure: %0.1f hPa" % bme280.pressure)
# print("Altitude: %0.1f" % bme280.altitude)
w.temp = (9/5) * bme280.temperature + 32
w.humidity = bme280.humidity
w.barometer = bme280.pressure
w.altitude = bme280.altitude