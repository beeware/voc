x = [1, 2, 3, 4, 5, 6]

print("x =", x)

print("Delete index 2...")
del x[2]
print("x =", x)

print("Delete index -1...")
del x[-1]
print("x =", x)

try:
    print("Delete index 10...")
    del x[10]
    print("Index shouldn't exist")
except IndexError:
    print("Index doesn't exist")

print("x =", x)

print("Done.")
