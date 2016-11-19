try:
    print('>>> x = NotImplemented')
    print('>>> +x')
    x = NotImplemented
    print(+x)
except Exception as e:
    print(type(e), ':', e)
print()
