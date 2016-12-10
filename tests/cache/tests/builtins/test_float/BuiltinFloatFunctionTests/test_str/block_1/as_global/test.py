try:
    print('>>> f = float')
    print('>>> x = ""')
    print('>>> f(x)')
    f = float
    x = ""
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = float')
    print('>>> x = "3"')
    print('>>> f(x)')
    f = float
    x = "3"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = float')
    print('>>> x = "This is another string"')
    print('>>> f(x)')
    f = float
    x = "This is another string"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = float')
    print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
    print('>>> f(x)')
    f = float
    x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = float')
    print('>>> x = "One arg: %s"')
    print('>>> f(x)')
    f = float
    x = "One arg: %s"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = float')
    print('>>> x = "Three args: %s | %s | %s"')
    print('>>> f(x)')
    f = float
    x = "Three args: %s | %s | %s"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
