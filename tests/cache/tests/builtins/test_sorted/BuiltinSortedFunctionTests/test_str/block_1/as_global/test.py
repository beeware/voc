try:
    print('>>> f = sorted')
    print('>>> x = ""')
    print('>>> f(x)')
    f = sorted
    x = ""
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = sorted')
    print('>>> x = "3"')
    print('>>> f(x)')
    f = sorted
    x = "3"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = sorted')
    print('>>> x = "This is another string"')
    print('>>> f(x)')
    f = sorted
    x = "This is another string"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = sorted')
    print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
    print('>>> f(x)')
    f = sorted
    x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = sorted')
    print('>>> x = "One arg: %s"')
    print('>>> f(x)')
    f = sorted
    x = "One arg: %s"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = sorted')
    print('>>> x = "Three args: %s | %s | %s"')
    print('>>> f(x)')
    f = sorted
    x = "Three args: %s | %s | %s"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
