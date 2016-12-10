try:
    print('>>> x = {}')
    print('>>> ~x')
    x = {}
    print(~x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> ~x')
    x = {"a": 1, "c": 2.3456, "d": "another"}
    print(~x)
except Exception as e:
    print(type(e), ':', e)
print()
