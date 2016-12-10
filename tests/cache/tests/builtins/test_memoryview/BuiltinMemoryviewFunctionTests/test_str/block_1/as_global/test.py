try:
    print('>>> f = memoryview')
    print('>>> x = ""')
    print('>>> f(x)')
    f = memoryview
    x = ""
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = memoryview')
    print('>>> x = "3"')
    print('>>> f(x)')
    f = memoryview
    x = "3"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = memoryview')
    print('>>> x = "This is another string"')
    print('>>> f(x)')
    f = memoryview
    x = "This is another string"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = memoryview')
    print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
    print('>>> f(x)')
    f = memoryview
    x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = memoryview')
    print('>>> x = "One arg: %s"')
    print('>>> f(x)')
    f = memoryview
    x = "One arg: %s"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = memoryview')
    print('>>> x = "Three args: %s | %s | %s"')
    print('>>> f(x)')
    f = memoryview
    x = "Three args: %s | %s | %s"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
