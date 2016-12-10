try:
    print('>>> x = ""')
    print('>>> y = True')
    print('>>> x //= y')
    print('>>> x')
    x = ""
    y = True
    x //= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = ""')
    print('>>> y = False')
    print('>>> x //= y')
    print('>>> x')
    x = ""
    y = False
    x //= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = "3"')
    print('>>> y = True')
    print('>>> x //= y')
    print('>>> x')
    x = "3"
    y = True
    x //= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = "3"')
    print('>>> y = False')
    print('>>> x //= y')
    print('>>> x')
    x = "3"
    y = False
    x //= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = "This is another string"')
    print('>>> y = True')
    print('>>> x //= y')
    print('>>> x')
    x = "This is another string"
    y = True
    x //= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = "This is another string"')
    print('>>> y = False')
    print('>>> x //= y')
    print('>>> x')
    x = "This is another string"
    y = False
    x //= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
    print('>>> y = True')
    print('>>> x //= y')
    print('>>> x')
    x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
    y = True
    x //= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
    print('>>> y = False')
    print('>>> x //= y')
    print('>>> x')
    x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
    y = False
    x //= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = "One arg: %s"')
    print('>>> y = True')
    print('>>> x //= y')
    print('>>> x')
    x = "One arg: %s"
    y = True
    x //= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = "One arg: %s"')
    print('>>> y = False')
    print('>>> x //= y')
    print('>>> x')
    x = "One arg: %s"
    y = False
    x //= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = "Three args: %s | %s | %s"')
    print('>>> y = True')
    print('>>> x //= y')
    print('>>> x')
    x = "Three args: %s | %s | %s"
    y = True
    x //= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = "Three args: %s | %s | %s"')
    print('>>> y = False')
    print('>>> x //= y')
    print('>>> x')
    x = "Three args: %s | %s | %s"
    y = False
    x //= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
