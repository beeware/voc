try:
    print('>>> f = bytearray')
    print('>>> x = ""')
    print('>>> f(x)')
    f = bytearray
    x = ""
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = bytearray')
    print('>>> x = "3"')
    print('>>> f(x)')
    f = bytearray
    x = "3"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = bytearray')
    print('>>> x = "This is another string"')
    print('>>> f(x)')
    f = bytearray
    x = "This is another string"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = bytearray')
    print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
    print('>>> f(x)')
    f = bytearray
    x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = bytearray')
    print('>>> x = "One arg: %s"')
    print('>>> f(x)')
    f = bytearray
    x = "One arg: %s"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = bytearray')
    print('>>> x = "Three args: %s | %s | %s"')
    print('>>> f(x)')
    f = bytearray
    x = "Three args: %s | %s | %s"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
