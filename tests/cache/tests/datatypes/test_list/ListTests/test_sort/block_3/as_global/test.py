def second(s):
    return s[1]

x = ['abc', 'bza', 'cda', 'daa']
x.sort(key=second)
print(x)
