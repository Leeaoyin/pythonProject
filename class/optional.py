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
    list_i.pop(len(list_i) - 1)
    print(list_i)


def tuple_in():
    t = ('lee', 21, True, '湖北')
    """遍历元组"""
    for elem in t:
        print(elem)
    """将元组转换成list"""
    person = list(t)
    print(person)
    """将list转换成tuple"""
    person_list = ['lee', 'xue', 'liu', 'wang']
    person_tuple = tuple(person_list)
    print(type(person_tuple))


def set_in():
    set_one = {1, 2, 3, 4, 5, 6, 7}
    set_two = set(range(1, 10))
    set_three = set(('a', 'c', 'd', 'e'))
    print(set_one, set_two)
    print(set_one)
    set_one.update([11, 12])
    print(set_one)
    print(set_three.pop())
    print(set_three)
    print(set_one & set_two)


def dict_in():
    scoces = {'lee': 21, 'june': 32, 'tom': 45, 'alice': 67}
    print(scoces)
    # 创建字典的构造器语法
    item_one = dict(one=1, tow=2, three=3)
    print(item_one)
    # 使用zip将两个序列压缩成字典
    tuple = ('lee', 12, True)
    tu = ('lee', 12, True)
    item_tow = dict(zip(tu, tuple))
    print(item_tow)


def main():
    # print("hello")
    # student = Student('Liming', 18)
    # student.study('python')
    # list_operation()
    # tuple_in()
    # set_in()
    dict_in()


if __name__ == '__main__':
    main()
