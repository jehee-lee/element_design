import RPi.GPIO as GPIO
import threading

relay = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay, GPIO.OUT)

def relay_test():
    global relay
    GPIO.output(relay, not GPIO.input(relay))
    print(GPIO.input(relay))
    
def thread_run():
    relay_test()
    threading.Timer(2,thread_run, [GPIO]).start()

try:
    thread_run()
    
except KeyboardInterrupt:
    GPIO.cleanup()
finally:
    GPIO.cleanup()