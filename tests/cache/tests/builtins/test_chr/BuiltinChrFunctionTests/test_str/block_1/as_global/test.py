try:
    print('>>> f = chr')
    print('>>> x = ""')
    print('>>> f(x)')
    f = chr
    x = ""
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = chr')
    print('>>> x = "3"')
    print('>>> f(x)')
    f = chr
    x = "3"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = chr')
    print('>>> x = "This is another string"')
    print('>>> f(x)')
    f = chr
    x = "This is another string"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = chr')
    print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
    print('>>> f(x)')
    f = chr
    x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = chr')
    print('>>> x = "One arg: %s"')
    print('>>> f(x)')
    f = chr
    x = "One arg: %s"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = chr')
    print('>>> x = "Three args: %s | %s | %s"')
    print('>>> f(x)')
    f = chr
    x = "Three args: %s | %s | %s"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
