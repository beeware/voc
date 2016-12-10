def test_function():
    import example.submodule
    
    example.submodule.some_method()
    
    print("Done.")
    
test_function()