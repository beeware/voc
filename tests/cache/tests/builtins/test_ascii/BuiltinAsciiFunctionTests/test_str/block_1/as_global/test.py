try:
    print('>>> f = ascii')
    print('>>> x = ""')
    print('>>> f(x)')
    f = ascii
    x = ""
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = ascii')
    print('>>> x = "3"')
    print('>>> f(x)')
    f = ascii
    x = "3"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = ascii')
    print('>>> x = "This is another string"')
    print('>>> f(x)')
    f = ascii
    x = "This is another string"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = ascii')
    print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
    print('>>> f(x)')
    f = ascii
    x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = ascii')
    print('>>> x = "One arg: %s"')
    print('>>> f(x)')
    f = ascii
    x = "One arg: %s"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = ascii')
    print('>>> x = "Three args: %s | %s | %s"')
    print('>>> f(x)')
    f = ascii
    x = "Three args: %s | %s | %s"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
