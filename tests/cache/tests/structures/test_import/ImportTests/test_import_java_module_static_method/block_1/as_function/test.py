def test_function():
    from java import lang
    
    props = lang.System.getProperties()
    print(props.get("file.separator"))
    
    print("Done.")
    
test_function()