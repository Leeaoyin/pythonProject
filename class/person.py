# -*- coding: utf-8 -*-
"""
#@File : person.py
#@Author : aoyinli@jksh.com
#@Time : 2022/5/6 19:34
#@Description : TODO
"""

class Person(object):

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # 访问器 - getter方法
    @property
    def name(self):
        return self.__name

    # 访问器 - getter方法
    @property
    def age(self):
        return self.__age

    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self.__age = age

    @name.setter
    def name(self, name):
        self.__name = name

    def play(self):
        if self.__age <= 16:
            print('%s正在玩飞行棋.' % self.__name)
        else:
            print('%s正在玩斗地主.' % self.__name)


def main():
    person = Person('王大锤', 12)
    print(person.age)
    person.play()
    person.age = 22
    person.play()
    # person.name = '白元芳'  # AttributeError: can't set attribute


if __name__ == '__main__':
    main()
