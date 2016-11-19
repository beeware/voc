pairs = [
    (1, 2, 3), (3, 2, 1),
    (1, 2, 1), (1, 2, 4),
    (1, 2, 3, 4), (1, 2, 3, 0)
]
for p1 in pairs:
    for p2 in pairs:
        print(p1, "<", p2, ":", p1 < p2)
