#%%
'''Задача 1:  Программа считывает натуральное число. По данному натуральному числу 
найдите минимальное натуральное число, состоящее из тех же цифр,
что и данное, и выведите его на экран.'''

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


#%%
"""Даны N точек на прямой. У каждой известны координата X и масса M. 
Задача: вывести координаты точек в порядке убывания массы."""

N = int(input())
param = []
for i in range(N):
    p = str(input()).split()
    m = int(p[1])
    if m > 0:
        param.append(p)
param = sorted(param, key = lambda x: x[1], reverse=True)
for i in range(len(param)):
    print(param[i][0])


# %%
"""Программа считывает URL-адрес сайта (например, https://vk.com). 
Определите, находится ли сайт в международном домене, и если нет, 
к какой стране он относится."""

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

