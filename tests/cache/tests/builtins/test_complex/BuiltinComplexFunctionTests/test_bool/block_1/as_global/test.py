try:
    print('>>> f = complex')
    print('>>> x = True')
    print('>>> f(x)')
    f = complex
    x = True
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = complex')
    print('>>> x = False')
    print('>>> f(x)')
    f = complex
    x = False
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
