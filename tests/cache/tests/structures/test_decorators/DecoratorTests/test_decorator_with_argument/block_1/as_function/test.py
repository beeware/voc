def test_function():
    def thing(multiplier):
        def _dec(fn):
            def _fn(value):
                print("Start decoration.")
                result = fn(value)
                print("End decoration.")
                return result * multiplier
            return _fn
        return _dec
    
    @thing(42)
    def calculate(value):
        print("Do a calculation")
        return 37 * value
    
    print("Decorated result is", calculate(5))
    print("Done.")
    
test_function()