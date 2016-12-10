def test_function():
    from java.lang import StringBuilder
    
    buf = StringBuilder()
    buf.append('Hello, ')
    buf.append('World')
    print(buf.toString())
    
    print("Done.")
    
test_function()