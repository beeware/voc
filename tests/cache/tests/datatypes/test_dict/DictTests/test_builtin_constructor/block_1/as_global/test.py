x = dict()
print(x)
print('a' in x)

# List of tuples
x = dict([('a', 1), ('b', 2)])
print('a' in x)
print(x['a'])
print('c' in x)

# List of lists
x = dict([['a', 3], ['b', 4]])
print('a' in x)
print(x['a'])
print('c' in x)

# Tuple of lists
x = dict((['a', 5], ['b', 6]))
print('a' in x)
print(x['a'])
print('c' in x)

# Tuple of tuples
x = dict((('a', 5), ('b', 6)))
print('a' in x)
print(x['a'])
print('c' in x)

# Test __contains__ throws unhashable exception
print([] in x)
print([] not in x)
