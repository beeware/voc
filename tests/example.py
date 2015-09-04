

class Point:
    def __init__(self, x, y, z):
        self.x = 37
        self.y = 42
        self.z = 6

    def distance(self):
        return self.x ** 2 + self.y ** 2 + self.z ** 2


def foo():
    for i in range(0, 10):
        print("FOR LOOP", i)
    print("All done")


def bar():
    i = 0
    while i < 10:
        print("WHILE LOOP", i)
        i += 1
    print("All done")

# class Point3D(Point):
#     def __init__(self):
#         pass


def body(value):
    print('Come, let us sail for the new world.', value)

    x = 6
    y = 9
    z = x * y

    print ("Answer is", z)

    print('Create point')
    p = Point(2, 3, 4)
    print('Distance with default is', p.distance())
    return 123

if __name__ == '__main__':
    print("Hello world")
    result = body(42)
    print("Result is", result)

    p = Point(2, 3, 4)
    print("Hello world", p)
    print ("attr x =", p.x)

    print("Method is", p.distance)
    print ("Distance is:", p.distance())
    # print("No such attribute", p.no_such_attribute)
    foo()
    bar()
