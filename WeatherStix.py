# 12JUN2020 : Written: JMK : Create focal point of this project;
#   define a data record and elementary data functions in a class object


class WeatherStix:
    '''This class represents the weather detail data being reported'''

    def __init__(self, datetime, precip, temp, humidity, windspeed, avgwindspeed2m,
                 winddirection, avgwinddirection2m, windgust, windgustdir, windgust10m,
                 windgustdir10m, battery, barometer, lightlevel, altitude):
        self.datetime = datetime
        self.precip = precip
        self.temp = temp
        self.humidity = humidity
        self.windspeed = windspeed
        self.avgwindspeed2m = avgwindspeed2m
        self.winddirection = winddirection
        self.avgwinddirection2m = avgwinddirection2m
        self.windgust = windgust
        self.windgustdir = windgustdir
        self.windgust10m = windgust10m
        self.windgustdir10m = windgustdir10m
        self.battery = battery
        self.barometer = barometer
        self.lightlevel = lightlevel
        self.altitude = altitude
