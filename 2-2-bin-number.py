import RPi.GPIO as GPIO
import time as t
dac = [8, 11, 7, 1, 0, 5, 12, 6]
number =[1, 0, 0, 0, 0, 0, 0, 0]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.output(dac, number)
t.sleep(20)
GPIO.output(dac, 0)
GPIO.cleanup()