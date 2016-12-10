i = 0
while i < 10:
    i = i + 1
    print(i, i % 5)
    if i % 5 == 0:
        continue
    print("after")
print("Done")
