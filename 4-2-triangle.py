import RPi.GPIO as GPIO
from time import sleep

def doubl(n):
    a = [0]*8
    i = 7
    while n > 0:
        a[i] = n % 2
        n = n // 2
        i -= 1
    return(a)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
chp = 1
v = 0
t = 0
T = (256-1) * 2
try:
    period = float(input('Период : '))
    while True:
        GPIO.output(dac, doubl(v))

        if v == 0:
            chp = 1
        if v == 255:
            chp = 0
        
        if chp == 1:
            v += 1
        else:
            v -= 1

        sleep(period / T)
        t += 1
except ValueError:
    print('Неправильное значение')
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()