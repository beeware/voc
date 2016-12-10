try:
    print('>>> f = hasattr')
    print('>>> x = frozenset()')
    print('>>> y = ""')
    print('>>> f(x, y)')
    f = hasattr
    x = frozenset()
    y = ""
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hasattr')
    print('>>> x = frozenset()')
    print('>>> y = "3"')
    print('>>> f(x, y)')
    f = hasattr
    x = frozenset()
    y = "3"
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hasattr')
    print('>>> x = frozenset()')
    print('>>> y = "This is another string"')
    print('>>> f(x, y)')
    f = hasattr
    x = frozenset()
    y = "This is another string"
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hasattr')
    print('>>> x = frozenset()')
    print('>>> y = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
    print('>>> f(x, y)')
    f = hasattr
    x = frozenset()
    y = "Mÿ hôvèrçràft îß fûłl öf éêlś"
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hasattr')
    print('>>> x = frozenset()')
    print('>>> y = "One arg: %s"')
    print('>>> f(x, y)')
    f = hasattr
    x = frozenset()
    y = "One arg: %s"
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hasattr')
    print('>>> x = frozenset()')
    print('>>> y = "Three args: %s | %s | %s"')
    print('>>> f(x, y)')
    f = hasattr
    x = frozenset()
    y = "Three args: %s | %s | %s"
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hasattr')
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> y = ""')
    print('>>> f(x, y)')
    f = hasattr
    x = frozenset({1, 2.3456, "another"})
    y = ""
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hasattr')
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> y = "3"')
    print('>>> f(x, y)')
    f = hasattr
    x = frozenset({1, 2.3456, "another"})
    y = "3"
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hasattr')
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> y = "This is another string"')
    print('>>> f(x, y)')
    f = hasattr
    x = frozenset({1, 2.3456, "another"})
    y = "This is another string"
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hasattr')
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> y = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
    print('>>> f(x, y)')
    f = hasattr
    x = frozenset({1, 2.3456, "another"})
    y = "Mÿ hôvèrçràft îß fûłl öf éêlś"
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hasattr')
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> y = "One arg: %s"')
    print('>>> f(x, y)')
    f = hasattr
    x = frozenset({1, 2.3456, "another"})
    y = "One arg: %s"
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hasattr')
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> y = "Three args: %s | %s | %s"')
    print('>>> f(x, y)')
    f = hasattr
    x = frozenset({1, 2.3456, "another"})
    y = "Three args: %s | %s | %s"
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
