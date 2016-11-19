def test_function():
    try:
        print('outer try')
        try:
            print('inner try')
        except:
            print('inner except')
    except:
        print('outer except')
    
test_function()