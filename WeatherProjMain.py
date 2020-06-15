# Project control code for JMKWeather
# import busio
import datetime
import WeatherStix

w = WeatherStix
# (self, datetime, precip, temp, humidity, windspeed, avgwindspeed2m,
#                  winddirection, avgwinddirection2m, windgust, windgustdir, windgust10m,
#                  windgustdir10m, battery, barometer, lightlevel)
w.datetime = datetime
print(w.datetime)
