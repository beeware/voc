try:
    print('>>> f = help')
    print('>>> x = ""')
    print('>>> f(x)')
    f = help
    x = ""
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = help')
    print('>>> x = "3"')
    print('>>> f(x)')
    f = help
    x = "3"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = help')
    print('>>> x = "This is another string"')
    print('>>> f(x)')
    f = help
    x = "This is another string"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = help')
    print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
    print('>>> f(x)')
    f = help
    x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = help')
    print('>>> x = "One arg: %s"')
    print('>>> f(x)')
    f = help
    x = "One arg: %s"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = help')
    print('>>> x = "Three args: %s | %s | %s"')
    print('>>> f(x)')
    f = help
    x = "Three args: %s | %s | %s"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
