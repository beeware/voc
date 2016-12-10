def test_function():
    def fizz_buzz(start, stop):
        for i in range(start, stop):
            found = False
            if i % 2 == 0:
                yield 'fizz'
                found = True
            if i % 3 == 0:
                yield 'buzz'
                found = True
            if not found:
                yield i
    
    print(list(fizz_buzz(1, 20)))
    
test_function()