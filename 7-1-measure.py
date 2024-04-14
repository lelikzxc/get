import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

leds = (2, 3, 4, 17, 27, 22, 10, 9)
dac = (8, 11, 7, 1, 0, 5, 12, 6)

GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(dac, GPIO.OUT, initial=GPIO.HIGH)

comp=4
troyka=17 
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(value):
    return [int(i) for i in bin(value)[2:].zfill(8)]

def adc():
    val = 0
    for i in range(7, -1, -1):
        val += 2**i
        dac_value = decimal2binary(val)
        GPIO.output(dac, dac_value)
        time.sleep(0.001)
        comp_value = GPIO.input(comp)
        if comp_value != 0:
            val -= 2**i
    return val

try:
    data=[]
    U_c = 0

    print('Начало зарядки конденсатора')
    GPIO.output(troyka, GPIO.HIGH)
    time_start = time.time()

    while U_c < 256*0.97:
        U_c = adc()
        data.append(U_c * 3.3/256)
        GPIO.output(leds, decimal2binary(U_c))

    GPIO.output(troyka, GPIO.LOW)

    print('Начало разрядки конденсатора')
    while U_c > 256*0.02:
        U_c = adc()
        data.append(U_c * 3.3/256)
        GPIO.output(leds, decimal2binary(U_c))

    time_experiment = time.time() - time_start

    x=[i*time_experiment/len(data) for i in range(len(data))]
    plt.plot(x, data)
    plt.xlabel('$t, $c')
    plt.ylabel('$U, $В')
    plt.show()

    with open('data.txt', 'w') as f:
        for i in data:
            f.write('\n'.join(str(i)))
    with open('settings.txt', 'w') as f:
        f.write('\n'.join(str(1/(time_experiment/len(data)))))
        f.write('\n'.join(str(3.3/256)))
    
    print('Общая продолжительность эксперимента составила {:.2f} с'.format(time_experiment))
    print('Период одного измерения {:.2f} мс'.format(time_experiment/len(data)*1e3))
    print('Средняя частота дискретизации {:.f} Гц'.format(1/(time_experiment/len(data))))
    print('Шаг квантования АЦП {:.2f}'.format(3.3/256))

finally:
    GPIO.output(leds, 0)
    GPIO.output(dac, 0)
    GPIO.cleanup()