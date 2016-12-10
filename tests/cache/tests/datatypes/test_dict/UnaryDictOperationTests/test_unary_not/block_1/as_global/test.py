try:
    print('>>> x = {}')
    print('>>> not x')
    x = {}
    print(not x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> not x')
    x = {"a": 1, "c": 2.3456, "d": "another"}
    print(not x)
except Exception as e:
    print(type(e), ':', e)
print()
