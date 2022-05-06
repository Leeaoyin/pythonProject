# -*- coding: utf-8 -*-
"""
#@File : optional.py
#@Author : aoyinli@jksh.com
#@Time : 2022/5/6 14:26
#@Description : TODO
"""

class Student:
    """the beginning of clazz"""
    def __init__(self, name, age):
        """construct mothed"""
        self.name = name
        self.age = age

    def study(self, course_name):
        print(f'{self.name}{self.age}正在学 {course_name}')


def list_for():
    list_one = [1, 2, 3, 4, 5, 6]
    # list_one.insert(1,200)
    # list_one.append(300)
    """三种循环遍历方式"""
    for x in range(len(list_one)):
        print(f'第一种{list_one[x]}')

    for element in list_one:
        print(f'第二种{element}')

    for index, elem in enumerate(list_one):
        print(f'第三种：下标{index}，数值：{elem}')


def list_operation():
    """list 操作"""
    list_i = [1, 2, 3, 4, 5, 6, 7, 8]
    if 3 in list_i:
        list_i.append(9)
    print(list_i)
    list_i.reverse()
    print(list_i)
    list_i.pop(len(list_i)-1)
    print(list_i)


def tuple_in():
    t = ('lee', 21, True, '湖北')
    print(type(t))


def main():
    # print("hello")
    # student = Student('Liming', 18)
    # student.study('python')
    # list_operation()
    tuple_in()


if __name__ == '__main__':
    main()
