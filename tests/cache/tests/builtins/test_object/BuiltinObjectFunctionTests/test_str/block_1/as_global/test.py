try:
    print('>>> f = object')
    print('>>> x = ""')
    print('>>> f(x)')
    f = object
    x = ""
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = object')
    print('>>> x = "3"')
    print('>>> f(x)')
    f = object
    x = "3"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = object')
    print('>>> x = "This is another string"')
    print('>>> f(x)')
    f = object
    x = "This is another string"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = object')
    print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
    print('>>> f(x)')
    f = object
    x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = object')
    print('>>> x = "One arg: %s"')
    print('>>> f(x)')
    f = object
    x = "One arg: %s"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = object')
    print('>>> x = "Three args: %s | %s | %s"')
    print('>>> f(x)')
    f = object
    x = "Three args: %s | %s | %s"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
