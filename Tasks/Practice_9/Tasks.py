""" Task 1 """

import math

numbers = input().split()
a = int(numbers[0])
b = int(numbers[1])
nod = math.gcd(a, b)
print(nod)

""" Task 2 """

from datetime import datetime, time

def days_lived(year, month, day):
    diff = (datetime.now() - datetime(year, month, day)).days
    return diff

""" Task 3 """

import base64

message = input()
tobyte = message.encode('utf-8')
tobase = base64.urlsafe_b64encode(tobyte)
result = tobase.decode('utf-8')
print(result)