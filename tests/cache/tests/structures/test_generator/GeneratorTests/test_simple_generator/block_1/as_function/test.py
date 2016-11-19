def test_function():
    def multiplier(first, second):
        y = first * second
        yield y
        y *= second
        yield y
        y *= second
        yield y
        y *= second
        yield y
    
    print(list(multiplier(1, 20)))
    
test_function()