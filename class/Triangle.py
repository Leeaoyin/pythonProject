# -*- coding: utf-8 -*-
"""
#@File : Triangle.py
#@Author : aoyinli@jksh.com
#@Time : 2022/5/6 18:53
#@Description : TODO
"""


class Triangle:


    def __init__(self,a ,b ,c):
        self.__a = a
        self.__b = b
        self.__c = c


    def is_valid(a, b, c):
        return a+b>c and a+c>b and c+b>a

    def crecal(self):
        return self._a+self._b+self._c

    @property
    def a(self):
        return self.__a

    def seta(self, a):
        self.__a = a


def main():
    a, b, c = 3,4,5
    t = Triangle(3, 4, 5)
    print(Triangle.is_valid(a,b,c))
    t.seta(6)
    print(t.a)





if __name__ == '__main__':
    main()

