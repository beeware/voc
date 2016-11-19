def test_function():
    def thing(fn):
        def _dec(value):
            print("Start decoration.")
            result = fn(value)
            print("End decoration.")
            return result * 42
        return _dec
    
    @thing
    def calculate(value):
        print("Do a calculation")
        return 37 * value
    
    print("Decorated result is", calculate(5))
    print("Done.")
    
test_function()