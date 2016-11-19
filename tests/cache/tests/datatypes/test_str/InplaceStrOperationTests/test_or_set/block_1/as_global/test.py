try:
    print('>>> x = ""')
    print('>>> y = set()')
    print('>>> x |= y')
    print('>>> x')
    x = ""
    y = set()
    x |= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = ""')
    print('>>> y = {1, 2.3456, "another"}')
    print('>>> x |= y')
    print('>>> x')
    x = ""
    y = {1, 2.3456, "another"}
    x |= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = "3"')
    print('>>> y = set()')
    print('>>> x |= y')
    print('>>> x')
    x = "3"
    y = set()
    x |= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = "3"')
    print('>>> y = {1, 2.3456, "another"}')
    print('>>> x |= y')
    print('>>> x')
    x = "3"
    y = {1, 2.3456, "another"}
    x |= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = "This is another string"')
    print('>>> y = set()')
    print('>>> x |= y')
    print('>>> x')
    x = "This is another string"
    y = set()
    x |= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = "This is another string"')
    print('>>> y = {1, 2.3456, "another"}')
    print('>>> x |= y')
    print('>>> x')
    x = "This is another string"
    y = {1, 2.3456, "another"}
    x |= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
    print('>>> y = set()')
    print('>>> x |= y')
    print('>>> x')
    x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
    y = set()
    x |= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
    print('>>> y = {1, 2.3456, "another"}')
    print('>>> x |= y')
    print('>>> x')
    x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
    y = {1, 2.3456, "another"}
    x |= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = "One arg: %s"')
    print('>>> y = set()')
    print('>>> x |= y')
    print('>>> x')
    x = "One arg: %s"
    y = set()
    x |= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = "One arg: %s"')
    print('>>> y = {1, 2.3456, "another"}')
    print('>>> x |= y')
    print('>>> x')
    x = "One arg: %s"
    y = {1, 2.3456, "another"}
    x |= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = "Three args: %s | %s | %s"')
    print('>>> y = set()')
    print('>>> x |= y')
    print('>>> x')
    x = "Three args: %s | %s | %s"
    y = set()
    x |= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = "Three args: %s | %s | %s"')
    print('>>> y = {1, 2.3456, "another"}')
    print('>>> x |= y')
    print('>>> x')
    x = "Three args: %s | %s | %s"
    y = {1, 2.3456, "another"}
    x |= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
