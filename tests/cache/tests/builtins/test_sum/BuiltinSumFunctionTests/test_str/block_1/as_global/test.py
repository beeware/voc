try:
    print('>>> f = sum')
    print('>>> x = ""')
    print('>>> f(x)')
    f = sum
    x = ""
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = sum')
    print('>>> x = "3"')
    print('>>> f(x)')
    f = sum
    x = "3"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = sum')
    print('>>> x = "This is another string"')
    print('>>> f(x)')
    f = sum
    x = "This is another string"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = sum')
    print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
    print('>>> f(x)')
    f = sum
    x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = sum')
    print('>>> x = "One arg: %s"')
    print('>>> f(x)')
    f = sum
    x = "One arg: %s"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = sum')
    print('>>> x = "Three args: %s | %s | %s"')
    print('>>> f(x)')
    f = sum
    x = "Three args: %s | %s | %s"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
