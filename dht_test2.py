import time

import Adafruit_DHT



sensor = Adafruit_DHT.DHT11

# 온습도 센서와 라즈베리 파이는 아래와 같이 다이렉트로 연결

# Signal(녹색) - GPIO4 (Pin no. 7)

# Vcc(빨강) - 5V 전원 (Pin no. 2)

# Ground(검정) - GND (Pin no. 6)

pin = 17

try:

    while True :

        h, t = Adafruit_DHT.read_retry(sensor, pin)

        if h is not None and t is not None :

            print("Temperature = {0:0.1f}*C Humidity = {1:0.1f}%".format(t, h))

        else :

            print('Read error')

        time.sleep(0.5)



except KeyboardInterrupt:

    print("Terminated by Keyboard")

   
finally:

        print("End of Program")

