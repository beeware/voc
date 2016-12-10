def test_function():
    from example.submodule.subsubmodule import another
    
    another.another_method()
    
    print("Done.")
    
test_function()