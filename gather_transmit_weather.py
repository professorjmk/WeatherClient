#Gather_Transmit_Weather.py
# written: 29MAY2020; JMK ; Utilize multiple sensors to gather data about current weather and transmit data to web server

# using SPI
import board
import busio
import digitalio
import adafruit_bme280
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = gigitalio.DigitalInOut(board.D5)
bme280 = adafruit.bme280.Adafruit_BME280_SPI(spi, cs)

# temperature - The sensor temperature in degrees Celcius
# humidity - The percent humidity as a value from 0% - 100%
# pressure - The pressure in hPa
# altitude - The altitude in meters

print("\nTemperature: %0.1f C" % bme280.temperature)
print("Humidity: %0.1f %%" % bme280.humitity)
print("Pressure: %0.1f hPa" % bme280.pressure)
print("Altitude: %0.1f" % bme.altitude)