try:
    print('>>> f = repr')
    print('>>> x = ""')
    print('>>> f(x)')
    f = repr
    x = ""
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = repr')
    print('>>> x = "3"')
    print('>>> f(x)')
    f = repr
    x = "3"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = repr')
    print('>>> x = "This is another string"')
    print('>>> f(x)')
    f = repr
    x = "This is another string"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = repr')
    print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
    print('>>> f(x)')
    f = repr
    x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = repr')
    print('>>> x = "One arg: %s"')
    print('>>> f(x)')
    f = repr
    x = "One arg: %s"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = repr')
    print('>>> x = "Three args: %s | %s | %s"')
    print('>>> f(x)')
    f = repr
    x = "Three args: %s | %s | %s"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
