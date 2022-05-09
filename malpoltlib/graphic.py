# -*- coding: utf-8 -*-
"""
#@File : graphic.py
#@Author : aoyinli@jksh.com
#@Time : 2022/5/9 16:29
#@Description : TODO
"""
import random

import matplotlib.pyplot as plt


def graphic_re():
    x = []
    y = []

    for i in range(4):
        x.append(random.randint(0, 20))
        y.append(random.randint(2, 20))

    print(x)
    print(y)
    do_graphic(x, y)


def do_graphic(x, y):
    plt.plot(x, y, color='blue', marker='o')
    plt.axis([0, 20, 0, 20])
    plt.show()


def get_graphic():
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    import numpy as np
    def f(t):
        return np.exp(-t) * np.cos(2 * np.pi * t)

    t1 = np.arange(0.0, 5.0, 0.1)
    t2 = np.arange(0.0, 5.0, 0.02)

    plt.figure()
    plt.subplot(211)
    plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

    plt.subplot(212)
    plt.plot(t2, np.cos(2 * np.pi * t2), 'r--')
    plt.show()


if __name__ == '__main__':
    get_graphic()
