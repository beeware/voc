def test_function():
    from java.lang import System
    
    props = System.getProperties()
    print(props.get("file.separator"))
    
    print("Done.")
    
test_function()