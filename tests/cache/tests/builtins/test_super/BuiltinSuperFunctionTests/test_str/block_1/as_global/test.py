try:
    print('>>> f = super')
    print('>>> x = ""')
    print('>>> f(x)')
    f = super
    x = ""
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = super')
    print('>>> x = "3"')
    print('>>> f(x)')
    f = super
    x = "3"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = super')
    print('>>> x = "This is another string"')
    print('>>> f(x)')
    f = super
    x = "This is another string"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = super')
    print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
    print('>>> f(x)')
    f = super
    x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = super')
    print('>>> x = "One arg: %s"')
    print('>>> f(x)')
    f = super
    x = "One arg: %s"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = super')
    print('>>> x = "Three args: %s | %s | %s"')
    print('>>> f(x)')
    f = super
    x = "Three args: %s | %s | %s"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
