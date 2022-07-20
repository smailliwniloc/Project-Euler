#PE 9
for a in range(500):
    for b in range(a, 500):
        for c in range(b, 500):
            if a**2 + b**2 == c**2 and a + b + c == 1000:
                print(a)
                print(b)
                print(c)
                print(a*b*c)
                break
