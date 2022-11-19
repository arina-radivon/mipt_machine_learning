""" Task 1 """

num = list(input())
num.sort()
if num[0] == '0':
    for i in range(len(num)):
        if num[i] != '0':
            num[0] = num[i]
            num[i] = '0'
            break
num = ''.join(num)
print(int(num))


""" Task 2 """

N = int(input())
param = []
for i in range(N):
    p = str(input()).split()
    m = int(p[1])
    if m > 0:
        param.append(p)
param = sorted(param, key=lambda x: x[1], reverse=True)
for i in range(len(param)):
    print(param[i][0])


""" Task 3"""

dom = str(input()) + ' '
if '.uk ' in dom:
    print('Великобритания')
elif '.de ' in dom:
    print('Германия')
elif '.il ' in dom:
    print('Израиль')
elif '.in ' in dom:
    print('Индия')
elif '.kz ' in dom:
    print('Казахстан')
elif '.mm ' in dom:
    print('Мьянма')
elif '.om ' in dom:
    print('Оман')
elif '.ru ' in dom:
    print('Россия')
elif '.uz ' in dom:
    print('Узбекистан')
elif '.et ' in dom:
    print('Эфиопия')
else:
    print('Международный')
