# 12JUN2020 : Written: JMK : Create focal point of this project;
#   define a data record and elementary functions in a class object


class WeatherStix:
    '''This class represents the weather detail data being reported'''

    def __init__(self, datetime, precip, temp, humidity, windspeed, avgwindspeed2m,
                 winddirection, avgwinddirection2m, windgust, windgustdir, windgust10m,
                 windgustdir10m, battery, barometer, lightlevel):
        self.datetime = 0
        self.precip = 0.0
        self.temp = 0.0
        self.humidity = 0.0
        self.windspeed = 0.0
        self.avgwindspeed2m = 0.0
        self.winddirection = ""
        self.avgwinddirection2m = ""
        self.windgust = 0.0
        self.windgustdir = ""
        self.windgust10m = 0.0
        self.windgustdir10m = ""
        self.battery = 0.0
        self.barometer = 0.0
        self.lightlevel = 0.0
