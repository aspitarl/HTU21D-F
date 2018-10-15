import time
import board
import busio
from adafruit_htu21d import HTU21D

i2c = busio.I2C(board.SCL,board.SDA)
sensor = HTU21D(i2c)
 

while True:
    print("\nTemperature: " , sensor.temperature, "    Humidity: ", sensor.relative_humidity)
    with open("log.csv",'a+') as write_file:
        write_file.write(str(time.time()) + ", " + str(sensor.temperature) + ", " + str(sensor.relative_humidity) + "\n")
        
    time.sleep(60)
