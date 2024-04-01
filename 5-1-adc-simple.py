import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def dec2bin(d):
    return [int(bit) for bit in bin(d)[2:].zfill(8)]


def adc():
    for value in range(256):
        signal = dec2bin(value)
        GPIO.output(dac, signal)
        time.sleep(0.001)
        comparatorvalue = GPIO.input(comp)
        if comparatorvalue != 0:
            return value
            break
        else:
            pass
    return 255




try:
    while True:
        i = adc()
        voltage = 3.3 * i / 256
        print('{}, {:.2f} v'.format(i, voltage))


finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()