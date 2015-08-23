
class Point:
    def __init__(self, x, y, z=4):
        self.x = x
        self.y = y
        self.z = z

    def distance(self):
        return self.x ** 2 + self.y ** 2 + self.z ** 2


def body(value):
    print('Come, let us sail for the new world.', value)

    x = 6
    y = 9
    z = x * y

    print ("Answer is", z)


if __name__ == '__main__':
    body(42)
