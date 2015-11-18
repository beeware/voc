
# def foo(x):
#     for v in range(1, 6):
#         print (v**2)


# def bar(x):
#     # print("Hello", x)
#     result = [v**2 for v in x]
#     print(result)

# x = [1, 2, 3, 4, 5]

# foo(x)
# bar(x)


# x = [1, 2, 3, 4, 5]
# print([v**2 for v in x])

# result = [v**2 for v in x]
# print(result)


# class MyClass:
#     def __init__(self, val):
#         print("VAL: ", val)
#         self.value = val

#     def stuff(self, delta):
#         print("DELTA: ", delta)
#         return self.value + delta

# obj = MyClass(4)
# obj.stuff(5)

# print('Done.')

# import other

# other.some_method()

# print("Done.")

# import time

# # time.clock()
# print("Hello world")
# print("time.clock", time.clock)

# from time import clock

# print("Hello world")
# print("clock", clock())
# print("time.clock", time.clock())


# class Point:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z

    # def distance(self):
    #     return self.x ** 2 + self.y ** 2 + self.z ** 2

    # def distance_plus(self, delta):
    #     return self.x ** 2 + self.y ** 2 + self.z ** 2 + delta


# for i in range(0, 10):
#     print("FOR LOOP", i)
# print("All done")

# def forloop():
#     for i in range(0, 10):
#         print("FOR LOOP", i)
#     print("All done")

# forloop()

s = '\0'

# x = range(0, 5)
# print("x[0] = ", x[0])
# print("x[1] = ", x[1])
# print("x[3] = ", x[3])
# print("x[-1] = ", x[-1])
# print("x[5] = ", x[5])


# x = None
# if x is None:
#     print('1: is none')
# else:
#     print('1: is not none')
# print('Done 1.')

# x = 1
# if x is not None:
#     print('2: is not none')
# else:
#     print('2: is none')
# print('Done 2.')

# def foo():
#     x = None
#     if x is None:
#         print('Correct')
#     else:
#         print('Incorrect')
#     print('Done1')

#     if x is not None:
#         print('Correct2')
#     else:
#         print('Incorrect3')
#     print('Done.')

    # x = 1
    # if x is 1:
    #     print('Correct')
    # else:
    #     print('Incorrect')

    # print('---1')
    # if x is 5:
    #     print('Incorrect')
    # else:
    #     print('Correct')

    # print('---2')
    # if x is None:
    #     print('Incorrect')
    # else:
    #     print('Correct')

    # print('---3')
    # x = None
    # print('---3a')
    # if x is None:
    #     print('Correct')
    # else:
    #     print('Incorrect')
    # print('Done.')


# x = 1
# if x is 1:
#     print('Correct')
# else:
#     print('Incorrect')

# print('---1')
# if x is 5:
#     print('Incorrect')
# else:
#     print('Correct')

# print('---2')
# if x is None:
#     print('Incorrect')
# else:
#     print('Correct')

# print('---3')
# x = None
# print('---3a')
# if x is None:
#     print('Correct')
# else:
#     print('Incorrect')
# print('Done.')

# def bar():
#     i = 0
#     total = 0
#     while i < 10:
#         i += 1
#         total += i
#         print(i, total)
#     print('Done.')

# bar()
# foo()

# for i in range(0, 10):
#     print("GFOR LOOP", i)
# print("GAll done")

# try:
#     obj = int('asdf')
#     print('OK')
# finally:
#     print("Do final cleanup")
# print('Done.')

# def bar():
#     i = 0
#     while i < 10:
#         print("WHILE LOOP", i)
#         i += 1
#     print("All done")

# # class Point3D(Point):
# #     def __init__(self):
# #         pass


# def body(value):
#     print('Come, let us sail for the new world.', value)

#     import time

#     def otherinner(msg):
#         print(msg, time.time())

# #     otherinner('foo')

#     x = 6
#     y = 9
#     z = x * y

#     print ("Answer is", z)

#     print('Create point')
#     p = Point(2, 3, 4)

#     print('Distance with default is', p.distance())

#     return 123


# x = [1, 2, 3]
# a, b, c = x
# print(a)
# print(b)
# print(c)

# if __name__ == '__main__':
    # import time

    # def innermethod(msg):
    #     print("inner")
    #     print(msg)

    # print("Hello, mainline")
    # # foo()
    # # print("part 2")

    # print(innermethod)

    # print("part 3")

    # # innermethod()
    # innermethod('hello')
    # print("Hello, world")

    # for i in range(1, 10):
    #     print(i, i % 5)
    #     if i % 5 == 0:
    #         continue
    #         # print("div 5")
    #     print ("after")
    # print("Done")

    # print('---')
    # i = 0
    # while i < 10:
    #     i = i + 1
    #     print(i, i % 5)
    #     if i % 5 == 0:
    #         break
    #     print ("after")
    # print("Done")

    # print('---')
    # i = 0
    # while i < 10:
    #     i = i + 1
    #     print(i, i % 5)
    #     if i % 5 == 0:
    #         continue
    #     print ("after")
    # print("Done")

    # x = 3.14159
    # print("Pi is ", x)
    # result = body(42)
    # print("Result is", result)

    # p = Point(2, 3, 4)
    # print("Hello world", p)
    # print ("attr x =", p.x)

    # x = 10
    # y = 0

    # if x < 5:
    #     print("X is small")
    # else:
    #     print("X is large")

    # if y < 5:
    #     print("Y is small")
    # else:
    #     print("Y is large")

    # x = True
    # y = not x
    # print ("NOT? ", y)

    # try:
    #     print('pre')
    #     p.no_such_attribute
    #     x = 3
    #     print('post')
    # except (AttributeError, TypeError) as e:
    #     print("Got the error", e)
    # # # # # except (AttributeError, TypeError):
    # # # #     # print("Got the error")
    # # # # # except AttributeError as e:
    # # # #     # print("Got the error", e)
    # # # # # except AttributeError:
    # # #     # print("Got the error")
    # # except NameError as e:
    #     # print("Got the error", e)
    # # # except RuntimeError:
    # #     # print("Got the error")
    # # except:
    #     # print("Bucket")
    # else:
    #     print("Do else")
    # finally:
    #     print("Do finally")

    # print("Method is", p.distance)
    # print("Distance is:", p.distance())
    # print("Distance plus is:", p.distance_plus(100))

    # foo()
    # bar()

#     x = (1, 2, 3, 4, 5)
#     print("CONST TUPLE:", x)
#     print(x[0], x[-1])

#     a = 1
#     b = 2
#     c = 3
#     d = 4
#     e = 5
#     x = (a, b, c, d, e)
#     print("TUPLE", x)
#     print(x[0], x[-1])

#     x = [1, 2, 3, 4, 5]
#     print("CONST LIST", x)
#     print(x[0], x[-1])

#     a = 1
#     b = 2
#     c = 3
#     d = 4
#     e = 5
#     x = [a, b, c, d, e]
#     print("LIST:", x)
#     print(x[0], x[2], x[-1])

#     x[2] = 42
#     print(x[0], x[2], x[-1])
#     print(c)

#     del x[2]
#     print(x)
#     print(c)

#     a, b, c, d = x
#     print("SEQUENCE:", a, b, c, d)

    # x = [1, 2, 3, 4, 5]
    # result = [v**2 for v in x]
    # print(result)

    # total = 0
    # for i in [1, 2, 3, 5, 8, 13, 21]:
        # total = total + i
    # print(total)
