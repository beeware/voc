def test_function():
    for x in range(2):
        try:
            print('success', next(iter([])))
        except Exception:
            print('whoops')
    
test_function()