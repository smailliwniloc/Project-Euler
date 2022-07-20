#PE 25

Fibonnaci = [1,1]

next = 1
while next < 10**999:
    next = Fibonnaci[-1] + Fibonnaci[-2]
    Fibonnaci.append(next)

print(len(Fibonnaci))
