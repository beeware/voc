

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distance(self):
        return self.x ** 2 + self.y ** 2 + self.z ** 2

    def distance_plus(self, delta):
        return self.x ** 2 + self.y ** 2 + self.z ** 2 + delta


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
    print("Hello, world")
    x = 3.14159
    print("Pi is ", x)
    result = body(42)
    print("Result is", result)

    p = Point(2, 3, 4)
    print("Hello world", p)
    print ("attr x =", p.x)

    x = 10
    y = 0

    if x < 5:
        print("X is small")
    else:
        print("X is large")

    if y < 5:
        print("Y is small")
    else:
        print("Y is large")

    x = True
    y = not x
    print ("NOT? ", y)

    try:
        print('pre')
        p.no_such_attribute
        # x = 3
        print('post')
    except (AttributeError, TypeError) as e:
        print("Got the error", e)
    # # except (AttributeError, TypeError):
    #     # print("Got the error")
    # # except AttributeError as e:
    #     # print("Got the error", e)
    # # except AttributeError:
    #     # print("Got the error")
    except NameError as e:
        print("Got the error", e)
    except RuntimeError:
        print("Got the error")
    except:
        print("Bucket")
    else:
        print("Do else")
    finally:
        print("Do finally")

    print("Method is", p.distance)
    print("Distance is:", p.distance())
    print("Distance plus is:", p.distance_plus(100))

    foo()
    bar()

    x = (1, 2, 3, 4, 5)
    print("CONST TUPLE:", x)
    print(x[0], x[-1])

    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    x = (a, b, c, d, e)
    print("TUPLE", x)
    print(x[0], x[-1])

    x = [1, 2, 3, 4, 5]
    print("CONST LIST", x)
    print(x[0], x[-1])

    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    x = [a, b, c, d, e]
    print("LIST:", x)
    print(x[0], x[2], x[-1])

    x[2] = 42
    print(x[0], x[2], x[-1])
    print(c)

    del x[2]
    print(x)
    print(c)

    a, b, c, d = x
    print("SEQUENCE:", a, b, c, d)

    x = [1, 2, 3, 4, 5]
    result = [v**2 for v in x]
    print(result)

    total = 0
    for i in [1, 2, 3, 5, 8, 13, 21]:
        total = total + i
    print(total)
