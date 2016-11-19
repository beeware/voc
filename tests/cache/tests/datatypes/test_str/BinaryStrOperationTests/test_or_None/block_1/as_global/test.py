try:
    print('>>> x = ""')
    print('>>> y = None')
    print('>>> x | y')
    x = ""
    y = None
    print(x | y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = "3"')
    print('>>> y = None')
    print('>>> x | y')
    x = "3"
    y = None
    print(x | y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = "This is another string"')
    print('>>> y = None')
    print('>>> x | y')
    x = "This is another string"
    y = None
    print(x | y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
    print('>>> y = None')
    print('>>> x | y')
    x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
    y = None
    print(x | y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = "One arg: %s"')
    print('>>> y = None')
    print('>>> x | y')
    x = "One arg: %s"
    y = None
    print(x | y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = "Three args: %s | %s | %s"')
    print('>>> y = None')
    print('>>> x | y')
    x = "Three args: %s | %s | %s"
    y = None
    print(x | y)
except Exception as e:
    print(type(e), ':', e)
print()
