def test_function():
    values = [
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
    ]
    for x, y, z, in values:
        print(x, y, z)
    print('Done.')
    
test_function()