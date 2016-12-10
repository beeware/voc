def test_function():
    for s in ['hello, world', 'HEllo, WORLD', 'átomo', '']:
        print(s.capitalize())
        print(s.lower())
        # print(s.swap())
        # print(s.title())
        print(s.upper())
    
test_function()