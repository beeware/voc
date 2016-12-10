def test_function():
    x = 10
    print("Pre assert 1")
    assert x > 0
    print("Pre assert 2")
    assert x < 0
    print("Done.")
    
test_function()