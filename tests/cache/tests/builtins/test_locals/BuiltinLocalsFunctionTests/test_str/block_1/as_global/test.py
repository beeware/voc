try:
    print('>>> f = locals')
    print('>>> x = ""')
    print('>>> f(x)')
    f = locals
    x = ""
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = locals')
    print('>>> x = "3"')
    print('>>> f(x)')
    f = locals
    x = "3"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = locals')
    print('>>> x = "This is another string"')
    print('>>> f(x)')
    f = locals
    x = "This is another string"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = locals')
    print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
    print('>>> f(x)')
    f = locals
    x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = locals')
    print('>>> x = "One arg: %s"')
    print('>>> f(x)')
    f = locals
    x = "One arg: %s"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = locals')
    print('>>> x = "Three args: %s | %s | %s"')
    print('>>> f(x)')
    f = locals
    x = "Three args: %s | %s | %s"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
