try:
    print('>>> f = iter')
    print('>>> x = ""')
    print('>>> f(x)')
    f = iter
    x = ""
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = iter')
    print('>>> x = "3"')
    print('>>> f(x)')
    f = iter
    x = "3"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = iter')
    print('>>> x = "This is another string"')
    print('>>> f(x)')
    f = iter
    x = "This is another string"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = iter')
    print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
    print('>>> f(x)')
    f = iter
    x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = iter')
    print('>>> x = "One arg: %s"')
    print('>>> f(x)')
    f = iter
    x = "One arg: %s"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = iter')
    print('>>> x = "Three args: %s | %s | %s"')
    print('>>> f(x)')
    f = iter
    x = "Three args: %s | %s | %s"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
