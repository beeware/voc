def test_function():
    for i in range(1, 10):
        print(i, i % 5)
        if i % 5 == 0:
            continue
        print ("after")
    print("Done")
    
test_function()