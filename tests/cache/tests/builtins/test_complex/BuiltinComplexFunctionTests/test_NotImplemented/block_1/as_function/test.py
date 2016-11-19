def test_function():
    try:
        print('>>> f = complex')
        print('>>> x = NotImplemented')
        print('>>> f(x)')
        f = complex
        x = NotImplemented
        print(f(x))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()