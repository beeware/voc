try:
    print('>>> f = round')
    print('>>> x = ""')
    print('>>> f(x)')
    f = round
    x = ""
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = round')
    print('>>> x = "3"')
    print('>>> f(x)')
    f = round
    x = "3"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = round')
    print('>>> x = "This is another string"')
    print('>>> f(x)')
    f = round
    x = "This is another string"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = round')
    print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
    print('>>> f(x)')
    f = round
    x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = round')
    print('>>> x = "One arg: %s"')
    print('>>> f(x)')
    f = round
    x = "One arg: %s"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = round')
    print('>>> x = "Three args: %s | %s | %s"')
    print('>>> f(x)')
    f = round
    x = "Three args: %s | %s | %s"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
