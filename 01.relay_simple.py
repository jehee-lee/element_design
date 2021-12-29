import RPi.GPIO as GPIO
import time

relay = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay, GPIO.OUT)


try:
    while(True):
        GPIO.output(relay, not GPIO.input(relay))
        time.sleep(2)
        
    
    

except KeyboardInterrupt:
    GPIO.cleanup()

finally:
    GPIO.cleanup()
