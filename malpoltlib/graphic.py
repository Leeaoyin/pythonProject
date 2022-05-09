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


if __name__ == '__main__':
    graphic_re()
