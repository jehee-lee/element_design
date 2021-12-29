import Adafruit_DHT
import time

sensor = Adafruit_DHT.DHT11
pin = 17

humid, temp = Adafruit_DHT.read_retry(sensor, pin)

while(1):
    try:
        time.sleep(1)
        if humid is not None and temp is not None:
            print('Temp = {0:0.1f}*C Humidity={1:0.1f}%'. format(temp, humid))
        else:
            print('Failed to get reading. Try again!')
            
    except:
        print("Error")