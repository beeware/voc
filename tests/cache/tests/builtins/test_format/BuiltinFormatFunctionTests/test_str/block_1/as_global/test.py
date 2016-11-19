try:
    print('>>> f = format')
    print('>>> x = ""')
    print('>>> f(x)')
    f = format
    x = ""
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = format')
    print('>>> x = "3"')
    print('>>> f(x)')
    f = format
    x = "3"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = format')
    print('>>> x = "This is another string"')
    print('>>> f(x)')
    f = format
    x = "This is another string"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = format')
    print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
    print('>>> f(x)')
    f = format
    x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = format')
    print('>>> x = "One arg: %s"')
    print('>>> f(x)')
    f = format
    x = "One arg: %s"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = format')
    print('>>> x = "Three args: %s | %s | %s"')
    print('>>> f(x)')
    f = format
    x = "Three args: %s | %s | %s"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
