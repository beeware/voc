try:
    print('>>> f = oct')
    print('>>> x = ""')
    print('>>> f(x)')
    f = oct
    x = ""
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = oct')
    print('>>> x = "3"')
    print('>>> f(x)')
    f = oct
    x = "3"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = oct')
    print('>>> x = "This is another string"')
    print('>>> f(x)')
    f = oct
    x = "This is another string"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = oct')
    print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
    print('>>> f(x)')
    f = oct
    x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = oct')
    print('>>> x = "One arg: %s"')
    print('>>> f(x)')
    f = oct
    x = "One arg: %s"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = oct')
    print('>>> x = "Three args: %s | %s | %s"')
    print('>>> f(x)')
    f = oct
    x = "Three args: %s | %s | %s"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
