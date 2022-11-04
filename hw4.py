"""Задача 1: Напишите функцию fibonacci(index), 
которая находит число Фибоначчи с нужным номером. 
Аргумент функции index — целое положительное число."""


def fibonacci(index):
    if index == 1:
        return 0
    elif index == 2:
        return 1
    else:
        f = [0, 1]
        for i in range(index):
            if i > 1:
                f.append(f[i-2]+f[i-1])
        return f[-1]


"""Задача 2: Напишите функцию last_discharge(a), которая в качестве аргумента
 получает строку, содержащую число a, и возвращает это же число,
  уменьшенное на единицу в последнем его разряде в виде строки."""


def last_discharge(a: str):
    if '.' not in a:
        res = str(int(a) - 1)
    elif '.' in a:
        vych = '0.'
        dot_ind = a.find('.') + 1
        while dot_ind != len(a)-1:
            vych += '0'
            dot_ind += 1
        vych += '1'
        res = str(float(a) - float(vych))
    return res


"""Задача 3: Программа считывает со стандартного потока ввода полный путь
к текстовому файлу. В файле содержится множество слов. Напишите программу,
которая будет считывать и выводить, сколько раз встречается каждое слово."""

words = dict()
filename = input()
with open(filename) as f:
    for row in f:
        line = row.split()
        for word in line:
            if word not in words:
                words[word] = 1
            else:
                words[word] += 1
w = dict(sorted(words.items(), key=lambda items: (-items[1], items[0])))
for element in w.keys():
    print(w[element], element)
