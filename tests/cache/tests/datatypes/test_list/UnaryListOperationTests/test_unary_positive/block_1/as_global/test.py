try:
    print('>>> x = []')
    print('>>> +x')
    x = []
    print(+x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = [3, 4, 5]')
    print('>>> +x')
    x = [3, 4, 5]
    print(+x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
    print('>>> +x')
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(+x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = ["a","b","c"]')
    print('>>> +x')
    x = ["a","b","c"]
    print(+x)
except Exception as e:
    print(type(e), ':', e)
print()
