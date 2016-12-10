try:
    print('>>> f = getattr')
    print('>>> x = b""')
    print('>>> y = ""')
    print('>>> f(x, y)')
    f = getattr
    x = b""
    y = ""
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = b""')
    print('>>> y = "3"')
    print('>>> f(x, y)')
    f = getattr
    x = b""
    y = "3"
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = b""')
    print('>>> y = "This is another string"')
    print('>>> f(x, y)')
    f = getattr
    x = b""
    y = "This is another string"
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = b""')
    print('>>> y = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
    print('>>> f(x, y)')
    f = getattr
    x = b""
    y = "Mÿ hôvèrçràft îß fûłl öf éêlś"
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = b""')
    print('>>> y = "One arg: %s"')
    print('>>> f(x, y)')
    f = getattr
    x = b""
    y = "One arg: %s"
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = b""')
    print('>>> y = "Three args: %s | %s | %s"')
    print('>>> f(x, y)')
    f = getattr
    x = b""
    y = "Three args: %s | %s | %s"
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = b"This is another string of bytes"')
    print('>>> y = ""')
    print('>>> f(x, y)')
    f = getattr
    x = b"This is another string of bytes"
    y = ""
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = b"This is another string of bytes"')
    print('>>> y = "3"')
    print('>>> f(x, y)')
    f = getattr
    x = b"This is another string of bytes"
    y = "3"
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = b"This is another string of bytes"')
    print('>>> y = "This is another string"')
    print('>>> f(x, y)')
    f = getattr
    x = b"This is another string of bytes"
    y = "This is another string"
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = b"This is another string of bytes"')
    print('>>> y = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
    print('>>> f(x, y)')
    f = getattr
    x = b"This is another string of bytes"
    y = "Mÿ hôvèrçràft îß fûłl öf éêlś"
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = b"This is another string of bytes"')
    print('>>> y = "One arg: %s"')
    print('>>> f(x, y)')
    f = getattr
    x = b"This is another string of bytes"
    y = "One arg: %s"
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = b"This is another string of bytes"')
    print('>>> y = "Three args: %s | %s | %s"')
    print('>>> f(x, y)')
    f = getattr
    x = b"This is another string of bytes"
    y = "Three args: %s | %s | %s"
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
