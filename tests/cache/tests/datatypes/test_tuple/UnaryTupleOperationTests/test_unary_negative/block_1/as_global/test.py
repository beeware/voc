try:
    print('>>> x = (1, 2)')
    print('>>> -x')
    x = (1, 2)
    print(-x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
    print('>>> -x')
    x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(-x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = (3, 1.2, True, )')
    print('>>> -x')
    x = (3, 1.2, True, )
    print(-x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = (1, 2.3456, "another")')
    print('>>> -x')
    x = (1, 2.3456, "another")
    print(-x)
except Exception as e:
    print(type(e), ':', e)
print()
