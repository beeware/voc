def test_function():
    x = float('0.0')
    print(x.hex())
    
    
    x = float('-0.0')
    print(x.hex())
    
    
    x = float('1.0000152587890625')
    print(x.hex())
    
    
    x = float('-5.66e+87')
    print(x.hex())
    
    
    x = float('-8.733636242518255e-261')
    print(x.hex())
    
    
    x = float('5e-324')
    print(x.hex())
    
    
    x = float('nan')
    print(x.hex())
    
    
    x = float('inf')
    print(x.hex())
    
    
    x = float('-inf')
    print(x.hex())
    
test_function()