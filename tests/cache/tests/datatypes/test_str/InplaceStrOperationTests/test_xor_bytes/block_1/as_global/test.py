try:
    print('>>> x = ""')
    print('>>> y = b""')
    print('>>> x ^= y')
    print('>>> x')
    x = ""
    y = b""
    x ^= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = ""')
    print('>>> y = b"This is another string of bytes"')
    print('>>> x ^= y')
    print('>>> x')
    x = ""
    y = b"This is another string of bytes"
    x ^= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = "3"')
    print('>>> y = b""')
    print('>>> x ^= y')
    print('>>> x')
    x = "3"
    y = b""
    x ^= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = "3"')
    print('>>> y = b"This is another string of bytes"')
    print('>>> x ^= y')
    print('>>> x')
    x = "3"
    y = b"This is another string of bytes"
    x ^= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = "This is another string"')
    print('>>> y = b""')
    print('>>> x ^= y')
    print('>>> x')
    x = "This is another string"
    y = b""
    x ^= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = "This is another string"')
    print('>>> y = b"This is another string of bytes"')
    print('>>> x ^= y')
    print('>>> x')
    x = "This is another string"
    y = b"This is another string of bytes"
    x ^= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
    print('>>> y = b""')
    print('>>> x ^= y')
    print('>>> x')
    x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
    y = b""
    x ^= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
    print('>>> y = b"This is another string of bytes"')
    print('>>> x ^= y')
    print('>>> x')
    x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
    y = b"This is another string of bytes"
    x ^= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = "One arg: %s"')
    print('>>> y = b""')
    print('>>> x ^= y')
    print('>>> x')
    x = "One arg: %s"
    y = b""
    x ^= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = "One arg: %s"')
    print('>>> y = b"This is another string of bytes"')
    print('>>> x ^= y')
    print('>>> x')
    x = "One arg: %s"
    y = b"This is another string of bytes"
    x ^= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = "Three args: %s | %s | %s"')
    print('>>> y = b""')
    print('>>> x ^= y')
    print('>>> x')
    x = "Three args: %s | %s | %s"
    y = b""
    x ^= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = "Three args: %s | %s | %s"')
    print('>>> y = b"This is another string of bytes"')
    print('>>> x ^= y')
    print('>>> x')
    x = "Three args: %s | %s | %s"
    y = b"This is another string of bytes"
    x ^= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
