try:
    print('>>> f = id')
    print('>>> x = ""')
    print('>>> f(x)')
    f = id
    x = ""
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = id')
    print('>>> x = "3"')
    print('>>> f(x)')
    f = id
    x = "3"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = id')
    print('>>> x = "This is another string"')
    print('>>> f(x)')
    f = id
    x = "This is another string"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = id')
    print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
    print('>>> f(x)')
    f = id
    x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = id')
    print('>>> x = "One arg: %s"')
    print('>>> f(x)')
    f = id
    x = "One arg: %s"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = id')
    print('>>> x = "Three args: %s | %s | %s"')
    print('>>> f(x)')
    f = id
    x = "Three args: %s | %s | %s"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
