def test_function():
    from java import lang
    
    buf = lang.StringBuilder()
    buf.append('Hello, ')
    buf.append('World')
    print(buf.toString())
    
    print("Done.")
    
test_function()