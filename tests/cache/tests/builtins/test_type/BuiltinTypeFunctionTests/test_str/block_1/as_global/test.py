try:
    print('>>> f = type')
    print('>>> x = ""')
    print('>>> f(x)')
    f = type
    x = ""
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = type')
    print('>>> x = "3"')
    print('>>> f(x)')
    f = type
    x = "3"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = type')
    print('>>> x = "This is another string"')
    print('>>> f(x)')
    f = type
    x = "This is another string"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = type')
    print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
    print('>>> f(x)')
    f = type
    x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = type')
    print('>>> x = "One arg: %s"')
    print('>>> f(x)')
    f = type
    x = "One arg: %s"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = type')
    print('>>> x = "Three args: %s | %s | %s"')
    print('>>> f(x)')
    f = type
    x = "Three args: %s | %s | %s"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
