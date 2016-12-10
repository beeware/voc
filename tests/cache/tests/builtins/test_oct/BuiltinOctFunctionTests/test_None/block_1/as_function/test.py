def test_function():
    try:
        print('>>> f = oct')
        print('>>> x = None')
        print('>>> f(x)')
        f = oct
        x = None
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()