# for循环
li = [1, 2, 4, 5, 8]
for i in li:
    print(i)

print('\n')

# 循环元祖
tr = (1, 2, 'a', 'sudo', 5)
for x in tr:
    print(x)


print('\n以下循环字典')
# 循环字典
di = {'name': 'leeaoyin', 'age': 1, 'sex': 'man'}
for d in di:
    print(di[d])

# 循环set
print('\n以下循环set')
se = set(['1231', '3434', 54654])
for s in se:
    print(s)

# 循环range
print('\n以下循环range')
for r in range(0, 10):
    print(r)

# while循环
i = 0
a = 1
while a <= 100:
    i = i+a
    a = a+1
    if a > 3:
        continue
print(i)

# 打印九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(i, j, i*j), end='')
    print()
