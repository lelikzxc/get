import RPi.GPIO as GPIO



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

try:
    while True:
        num = input('Введите число : ')
        try:
            num = int(num)
            if num >= 0 and num <= 255 :
                GPIO.output(dac, doubl(num))
                v = float(num) / 256.0 * 3.3
                print(f'Напряжение : {v:.3}')
            else:
                if num > 255 or num < 0:
                    print('Нельзя вывести это число')
        except Exception:
            if num == "q":
                print('Ввод закончен')
                break
            print('Неправильное значение')
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()