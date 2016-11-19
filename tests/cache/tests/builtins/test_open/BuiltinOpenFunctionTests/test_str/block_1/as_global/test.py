try:
    print('>>> f = open')
    print('>>> x = ""')
    print('>>> f(x)')
    f = open
    x = ""
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = open')
    print('>>> x = "3"')
    print('>>> f(x)')
    f = open
    x = "3"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = open')
    print('>>> x = "This is another string"')
    print('>>> f(x)')
    f = open
    x = "This is another string"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = open')
    print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
    print('>>> f(x)')
    f = open
    x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = open')
    print('>>> x = "One arg: %s"')
    print('>>> f(x)')
    f = open
    x = "One arg: %s"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = open')
    print('>>> x = "Three args: %s | %s | %s"')
    print('>>> f(x)')
    f = open
    x = "Three args: %s | %s | %s"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
