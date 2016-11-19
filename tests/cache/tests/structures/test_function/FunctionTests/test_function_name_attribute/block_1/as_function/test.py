def test_function():
    def myfunc():
        def otherfunc():
            pass
        print(otherfunc.__name__)
    
    print(myfunc.__name__)
    myfunc()
    
test_function()