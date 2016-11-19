iterable = [True, False, True]
def testish(x):
    return bool(x)
it = map(testish, iterable)
print(it)
print(next(it))
print(next(it))
print(next(it))
try:
    print(next(it))
except StopIteration:
    pass
