iterable = [1, 2, 3]
def testish(x):
    return x * 2
it = map(testish, iterable)
print(it)
print(next(it))
print(next(it))
print(next(it))
try:
    print(next(it))
except StopIteration:
    pass
