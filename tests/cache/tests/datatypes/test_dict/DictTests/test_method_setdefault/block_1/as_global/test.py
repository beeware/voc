x = {42: 'Babel'}
print(x.setdefault(42)) # should return Babel

print(x.setdefault(1)) # should return None
print(x[1] == None) # should be True

print(x.setdefault('David', 'Gilmour')) # should return 'Gilmour'

# Check unhashable exceptions
x.setdefault([], 42)
