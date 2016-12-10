def test_function():
    total = 0
    for i in range(0, 10, 2):
        total = total + i
        print(i, total)
    print('Done.')
    
test_function()