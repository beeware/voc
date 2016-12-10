try:
    print('>>> f = enumerate')
    print('>>> x = ""')
    print('>>> f(x)')
    f = enumerate
    x = ""
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = enumerate')
    print('>>> x = "3"')
    print('>>> f(x)')
    f = enumerate
    x = "3"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = enumerate')
    print('>>> x = "This is another string"')
    print('>>> f(x)')
    f = enumerate
    x = "This is another string"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = enumerate')
    print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
    print('>>> f(x)')
    f = enumerate
    x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = enumerate')
    print('>>> x = "One arg: %s"')
    print('>>> f(x)')
    f = enumerate
    x = "One arg: %s"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = enumerate')
    print('>>> x = "Three args: %s | %s | %s"')
    print('>>> f(x)')
    f = enumerate
    x = "Three args: %s | %s | %s"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
