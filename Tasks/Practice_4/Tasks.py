""" Task 1 """


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


""" Task 2 """


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


""" Task 3 """

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
