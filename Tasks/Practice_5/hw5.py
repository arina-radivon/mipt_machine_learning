"""Задача 1: класс с координатами точек, метод находит
    расстояние между 2мя точками"""


class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distance_to(self, other):
        return ((self.x - other.x) ** 2 +
                (self.y - other.y) ** 2 +
                (self.z - other.z) ** 2) ** 0.5


"""Задача 2: класс принимает концы отрезка, методы находят
длину отрезка и середину; Задача 3: добавить метод cos_to"""


class Segment3D:
    def __init__(self, p1: Point3D, p2: Point3D):
        self.p1 = p1
        self.p2 = p2

    def length(self):
        return ((self.p1.x - self.p2.x) ** 2 +
                (self.p1.y - self.p2.y) ** 2 +
                (self.p1.z - self.p2.z) ** 2) ** 0.5

    def middle(self):
        return Point3D(
            (self.p1.x + self.p2.x)/2,
            (self.p1.y + self.p2.y)/2,
            (self.p1.z + self.p2.z)/2
        )

    def cos_to(self, other):
        vec_1 = (
            (self.p2.x - self.p1.x),
            (self.p2.y - self.p1.y),
            (self.p2.z - self.p1.z)
            )
        vec_2 = (
            (other.p2.x - other.p1.x),
            (other.p2.y - other.p1.y),
            (other.p2.z - other.p1.z)
            )
        mod_vec_1 = (vec_1[0] ** 2 + vec_1[1] ** 2 + vec_1[2] ** 2) ** 0.5
        mod_vec_2 = (vec_2[0] ** 2 + vec_2[1] ** 2 + vec_2[2] ** 2) ** 0.5
        skal = vec_1[0]*vec_2[0] + vec_1[1]*vec_2[1] + vec_1[2]*vec_2[2]

        return abs(skal / (mod_vec_1 * mod_vec_2))


if __name__ == '__main__':
    p1 = Point3D(1, 2, 3)
    p2 = Point3D(2.5, 1, -2)
    print(p1.distance_to(p2))

    s = Segment3D(p1, p2)
    print(s.length())
    m = s.middle()
    print(type(m) == Point3D)

    s1 = Segment3D(Point3D(0, 0, 0), Point3D(1, 2, 3))
    s2 = Segment3D(Point3D(0, 0, 0), Point3D(1, 0, 0))
    print(s1.cos_to(s2))
