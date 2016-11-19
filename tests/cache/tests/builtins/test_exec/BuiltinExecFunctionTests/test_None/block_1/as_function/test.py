def test_function():
    try:
        print('>>> f = exec')
        print('>>> x = None')
        print('>>> f(x)')
        f = exec
        x = None
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()