def test_function():
    x = {'a': 1, 'b': 2}
    
    print(" Delete 'a'...")
    del x['a']
    print('x =', x)
    
    try:
        print(" Delete 'a'...")
        del x['a']
        print("Key 'a' shouldn't exist")
    except KeyError:
        print("Key 'a' doesn't exist")
    print('x =', x)
    
    try:
        print(" Delete 'c'...")
        del x['c']
        print("Key 'c' never existed")
    except KeyError:
        print("Key 'c' doesn't exist")
    print('x =', x)
    
    print("Done.")
    
test_function()