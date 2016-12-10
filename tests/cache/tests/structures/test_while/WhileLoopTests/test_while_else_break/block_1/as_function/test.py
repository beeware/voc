def test_function():
    i = 1
    j = 4
    while i < j:
        print(i)
        i = i + 1
        break
    else:
        print("Else")
    print("Done")
    
test_function()