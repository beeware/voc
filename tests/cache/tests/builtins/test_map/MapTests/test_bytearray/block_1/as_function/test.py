def test_function():
    iterable = b'123'
    def testish(x):
        return x
    it = map(testish, iterable)
    print(it)
    print(next(it))
    print(next(it))
    print(next(it))
    try:
        print(next(it))
    except StopIteration:
        pass
    
test_function()