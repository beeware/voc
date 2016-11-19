values = {
    'a': 1,
    'b': 2,
    'c': 3,
}
for k, v in values.items():
    print(k, v)
print('And once again...')
for item in values.items():
    print(item[0], item[1])
print('Done.')
