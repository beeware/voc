try:
    print('>>> f = __import__')
    print('>>> x = ""')
    print('>>> f(x)')
    f = __import__
    x = ""
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = __import__')
    print('>>> x = "3"')
    print('>>> f(x)')
    f = __import__
    x = "3"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = __import__')
    print('>>> x = "This is another string"')
    print('>>> f(x)')
    f = __import__
    x = "This is another string"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = __import__')
    print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
    print('>>> f(x)')
    f = __import__
    x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = __import__')
    print('>>> x = "One arg: %s"')
    print('>>> f(x)')
    f = __import__
    x = "One arg: %s"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = __import__')
    print('>>> x = "Three args: %s | %s | %s"')
    print('>>> f(x)')
    f = __import__
    x = "Three args: %s | %s | %s"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
