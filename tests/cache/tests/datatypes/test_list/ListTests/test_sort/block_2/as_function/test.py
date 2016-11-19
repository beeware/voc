def test_function():
    fixtures = [
        [9, 4, 7],
        ['beta', 'theta', 'alpha'],
    ]
    for x in fixtures:
        x.sort(reverse=True)
        print(x)
    
test_function()