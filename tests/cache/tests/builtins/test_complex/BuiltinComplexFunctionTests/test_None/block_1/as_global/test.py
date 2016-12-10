try:
    print('>>> f = complex')
    print('>>> x = None')
    print('>>> f(x)')
    f = complex
    x = None
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
