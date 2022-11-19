""" Task 1 """

m = int(input())
if m == 1:
    print('январь\nзима')
elif m == 2:
    print('февраль\nзима')
elif m == 3:
    print('март\nвесна')
elif m == 4:
    print('апрель\nвесна')
elif m == 5:
    print('май\nвесна')
elif m == 6:
    print('июнь\nлето')
elif m == 7:
    print('июль\nлето')
elif m == 8:
    print('август\nлето')
elif m == 9:
    print('сентябрь\nосень')
elif m == 10:
    print('октябрь\nосень')
elif m == 11:
    print('ноябрь\nосень')
elif m == 12:
    print('декабрь\nзима')
else:
    print('ошибка')


""" Task 2 """

n_sum = float(input())
f_sum = float(input())
proc = float(input())
mon = 0
while n_sum < f_sum:
    n_sum += n_sum*proc/100
    mon += 1
print(mon)


""" Task 3 """

N = int(input())
sum = 0
for i in range(1, N+1):
    sum += i*i
print(sum)
