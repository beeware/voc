def test_function():
    i = 0
    try:
        while 1:
            print("Loop", i)
            i = i + 1
            if i == 10:
                break
    finally:
        print("Done")
    
test_function()