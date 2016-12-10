try:
    print('>>> x = NotImplemented')
    print('>>> y = ""')
    print('>>> x **= y')
    print('>>> x')
    x = NotImplemented
    y = ""
    x **= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = NotImplemented')
    print('>>> y = "3"')
    print('>>> x **= y')
    print('>>> x')
    x = NotImplemented
    y = "3"
    x **= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = NotImplemented')
    print('>>> y = "This is another string"')
    print('>>> x **= y')
    print('>>> x')
    x = NotImplemented
    y = "This is another string"
    x **= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = NotImplemented')
    print('>>> y = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
    print('>>> x **= y')
    print('>>> x')
    x = NotImplemented
    y = "Mÿ hôvèrçràft îß fûłl öf éêlś"
    x **= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = NotImplemented')
    print('>>> y = "One arg: %s"')
    print('>>> x **= y')
    print('>>> x')
    x = NotImplemented
    y = "One arg: %s"
    x **= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = NotImplemented')
    print('>>> y = "Three args: %s | %s | %s"')
    print('>>> x **= y')
    print('>>> x')
    x = NotImplemented
    y = "Three args: %s | %s | %s"
    x **= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
