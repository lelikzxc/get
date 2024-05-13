from matplotlib import pyplot as plt
import numpy as np
from textwrap import wrap
from matplotlib.ticker import *
#import pandas as pd
from matplotlib.legend_handler import HandlerLine2D, HandlerTuple

with open('/home/b04-307/get/settings.txt') as settings:
    freq, step = map(float, settings.read().split('\n'))

data = np.loadtxt('/home/b04-307/get/data.txt', dtype = int)

U_arr = data * step
time_charge = len(data) / freq
time_arr = np.arange(0, time_charge, 1/freq)

fig = plt.figure(figsize = (5 * np.sqrt(2), 5), dpi = 180)

time_arr = np.delete(time_arr, 110)

ax1 = fig.add_subplot(111)
ax1.set_title('\n'.join(wrap('Процесс заряда конденсатора в RC-цепочке', 60)), loc = 'center', fontsize = 16)
ax1.plot(time_arr, U_arr, color = 'b', label = 'V(t)', markevery=range(0, len(data), 10), marker = 'o')

ax1.set_xlabel('Время, с', fontsize = 10)
ax1.set_ylabel('Напряжение, В', fontsize = 10)

box = dict(
    boxstyle = 'square, pad = 0.3',
    ec = 'k',
    fc = 'w',
    ls = '-',
    lw = 1
)

ax1.text(4, 1, 'Время зарядки конденсатора {:.2f} с'.format(time_charge), bbox = box, fontsize = 10)

ax1.set_xlim(0)
ax1.set_ylim(0)

ax1.xaxis.set_minor_locator(AutoMinorLocator(10))
ax1.yaxis.set_minor_locator(AutoMinorLocator(10))

ax1.minorticks_on()

ax1.set_axisbelow(True)

ax1.grid(which = 'major', linewidth = 0.7, alpha = 0.7)
ax1.grid(which = 'minor', linestyle = ':', linewidth = 0.5, alpha = 0.7)

ax1.yaxis.set_label_coords(-0.1, 0.5)
ax1.legend()

plt.show()