try:
    print('>>> x = ""')
    print('>>> +x')
    x = ""
    print(+x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = "3"')
    print('>>> +x')
    x = "3"
    print(+x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = "This is another string"')
    print('>>> +x')
    x = "This is another string"
    print(+x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = "Mÿ hôvèrçràft îß fûłl öf éêlś"')
    print('>>> +x')
    x = "Mÿ hôvèrçràft îß fûłl öf éêlś"
    print(+x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = "One arg: %s"')
    print('>>> +x')
    x = "One arg: %s"
    print(+x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = "Three args: %s | %s | %s"')
    print('>>> +x')
    x = "Three args: %s | %s | %s"
    print(+x)
except Exception as e:
    print(type(e), ':', e)
print()
