try:
    print('>>> f = all')
    print('>>> x = ""')
    print('>>> f(x)')
    f = all
    x = ""
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = all')
    print('>>> x = "3"')
    print('>>> f(x)')
    f = all
    x = "3"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = all')
    print('>>> x = "This is another string"')
    print('>>> f(x)')
    f = all
    x = "This is another string"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = all')
    print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
    print('>>> f(x)')
    f = all
    x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = all')
    print('>>> x = "One arg: %s"')
    print('>>> f(x)')
    f = all
    x = "One arg: %s"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = all')
    print('>>> x = "Three args: %s | %s | %s"')
    print('>>> f(x)')
    f = all
    x = "Three args: %s | %s | %s"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
