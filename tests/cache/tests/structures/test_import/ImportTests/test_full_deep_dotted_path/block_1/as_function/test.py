def test_function():
    import example.submodule.subsubmodule.another
    
    example.submodule.subsubmodule.another.another_method()
    
    print("Done.")
    
test_function()