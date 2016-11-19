iterable = [3.14, 2.17, 1.0]
def testish(x):
    return x > 1
it = map(testish, iterable)
print(it)
print(next(it))
print(next(it))
print(next(it))
try:
    print(next(it))
except StopIteration:
    pass
