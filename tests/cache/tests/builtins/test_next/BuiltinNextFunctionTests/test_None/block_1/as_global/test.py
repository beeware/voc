try:
    print('>>> f = next')
    print('>>> x = None')
    print('>>> f(x)')
    f = next
    x = None
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
