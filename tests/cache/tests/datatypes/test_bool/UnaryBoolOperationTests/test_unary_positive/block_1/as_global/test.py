try:
    print('>>> x = True')
    print('>>> +x')
    x = True
    print(+x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = False')
    print('>>> +x')
    x = False
    print(+x)
except Exception as e:
    print(type(e), ':', e)
print()
