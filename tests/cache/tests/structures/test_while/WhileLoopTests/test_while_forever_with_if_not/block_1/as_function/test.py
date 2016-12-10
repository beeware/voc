def test_function():
    i = 0
    while 1:
        print("Loop", i)
        i = i + 1
        if not i < 10:
            break
    print("Done")
    
test_function()