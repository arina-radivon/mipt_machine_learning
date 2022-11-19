""" Task 1 """


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        else:
            return False

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(other * self.x, other * self.y)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self * other

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        else:
            return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x/other, self.y/other)
        else:
            return NotImplemented

    def __abs__(self):
        return (self.x**2 + self.y**2)**0.5


""" Task 2 """


class Lucas:
    def __init__(self, u0, u1, p, q, n):
        self.first = u0
        self.second = u1
        self.p = p
        self.q = q
        self.n = n
        self.ind = 0

    def __iter__(self):
        return self

    def __next__(self):
        first, self.first, self.second = self.first, self.second, -1*self.first*self.q + self.second*self.p
        self.ind += 1
        if self.ind > self.n:
            raise StopIteration
        return first


""" Task 3 """


class Number:

    def __init__(self, number):
        self.number = number

    def __repr__(self):
        return str(self.number)

    def __getattr__(self, key):
        str_Number = str(self.number)
        if key == 'minus':
            return Number(str_Number+'-')
        elif key == 'plus':
            return Number(str_Number+'+')
        elif key == 'times':
            return Number(str_Number+'*')
        elif key == 'zero':
            return Number(eval(str_Number+'0'))
        elif key == 'one':
            return Number(eval(str_Number+'1'))
        elif key == 'two':
            return Number(eval(str_Number+'2'))
        elif key == 'three':
            return Number(eval(str_Number+'3'))
        elif key == 'four':
            return Number(eval(str_Number+'4'))
        elif key == 'five':
            return Number(eval(str_Number+'5'))
        elif key == 'six':
            return Number(eval(str_Number+'6'))
        elif key == 'seven':
            return Number(eval(str_Number+'7'))
        elif key == 'eight':
            return Number(eval(str_Number+'8'))
        elif key == 'nine':
            return Number(eval(str_Number+'9'))
        else:
            return NotImplemented


zero = Number(0)
one = Number(1)
two = Number(2)
three = Number(3)
four = Number(4)
five = Number(5)
six = Number(6)
seven = Number(7)
eight = Number(8)
nine = Number(9)

if __name__ == '__main__':
    print(list(Lucas(0, 1, 1, -1, 10)))
