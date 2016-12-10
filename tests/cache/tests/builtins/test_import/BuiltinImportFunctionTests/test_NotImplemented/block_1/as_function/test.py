def test_function():
    try:
        print('>>> f = __import__')
        print('>>> x = NotImplemented')
        print('>>> f(x)')
        f = __import__
        x = NotImplemented
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()