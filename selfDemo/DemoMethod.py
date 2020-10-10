# 条件判断 函数
def sumNum(s, m):
    """两个数相加"""
    if not (isinstance(s, (int, float))) and (isinstance(m, (int, float))):
        raise TypeError('参数类型错误')
    return s + m


b = sumNum('s', 'a')
print(b)


# 形参带默认值
def printMessage(name, sex, age=17):
    print('姓名：{}'.format(name))
    print('性别：{}'.format(sex))
    print('年龄：{}'.format(age))


name = 'lee'
sex = 'man'
printMessage('ao', 'woman', 200)
print('判断isinstance')


# 判断isinstance


# def isType(a, b):
#     print((isinstance(a, int)) and (isinstance(b, int)))
#     if (not isinstance(a, int)) and not (isinstance(b, int)):
#         raise TypeError('参数类型错误')
#     return a + b


# c = isType(2, 9)
# print(c)


def testNone(a, p=None):
    if p is None:
        p = []
    return p


# 判断默认值
_no_value = object()


def isNoValue(a, b=_no_value):
    if b is _no_value:
        print('b , 没有赋值')
    if (not isinstance(a, int)) or not (isinstance(b, int)):
        raise TypeError('参数类型错误')
    return a + b


x = isNoValue(2, 3)
print(x)


def toString(count, nmm=_no_value):
    if nmm is _no_value:
        raise TypeError('nmm参数没有赋值')
    if (isinstance(count, (int, float))) or (isinstance(nmm, (int, float))):
        raise ValueError('参数类型错误')
    final = count + nmm
    return final


print(toString('a', 'a'))


# 不定长参数


def print_user_info(age, na, se, *hobby):
    print("昵称：{}".format(na), end=' ')
    print('性别：{}'.format(se), end=' ')
    print('爱好：{}'.format(hobby))
    return


print_user_info(17, 'lee', 'man', '打球', '游戏')



