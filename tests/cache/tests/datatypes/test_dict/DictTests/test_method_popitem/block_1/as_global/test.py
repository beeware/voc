ITEMS = [(1, 2), (3, ("4", 5))]
x = dict(ITEMS)

popped_1 = x.popitem()
print(popped_1 in ITEMS)

popped_2 = x.popitem()
print(popped_2 in ITEMS and popped_2 != popped_1)

print(x.popitem()) # Check for exception
