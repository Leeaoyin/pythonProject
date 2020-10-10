# the first demo of python
yu = ('aaa', 3)
# 字典数据类型
dit = {'name': 'legion', 'age': '17'}
del dit['name']
age = dit['age']
print(dit)
# set数据类型
set1 = set([2, 4, 321,  1, 1, 5])
set2 = set([2, 1, 5, 7])
print(set1 | set2)
print('\n去除海量元素里的重复元素')
li = [1, 1, 1, 2, 5, 3, 2, 4, 7, 243,  'e', 'a', 'e', 7, 3]
set3 = set(li)
print(set3)

