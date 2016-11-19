try:
    print('>>> f = slice')
    print('>>> x = ""')
    print('>>> f(x)')
    f = slice
    x = ""
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = slice')
    print('>>> x = "3"')
    print('>>> f(x)')
    f = slice
    x = "3"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = slice')
    print('>>> x = "This is another string"')
    print('>>> f(x)')
    f = slice
    x = "This is another string"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = slice')
    print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
    print('>>> f(x)')
    f = slice
    x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = slice')
    print('>>> x = "One arg: %s"')
    print('>>> f(x)')
    f = slice
    x = "One arg: %s"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = slice')
    print('>>> x = "Three args: %s | %s | %s"')
    print('>>> f(x)')
    f = slice
    x = "Three args: %s | %s | %s"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
