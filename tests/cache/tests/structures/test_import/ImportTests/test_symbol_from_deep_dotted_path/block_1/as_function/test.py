def test_function():
    from example.submodule.subsubmodule.another import another_method
    
    another_method()
    
    print("Done.")
    
test_function()