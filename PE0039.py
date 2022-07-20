#PE 39

triples = []

for a in range(500):
    for b in range(a,500):
        for c in range(b,500):
            if a**2 + b**2 == c**2:
                triples.append([a,b,c])

dict = {}

for i in range(1500):
    dict[i] = 0

for nums in triples:
    perimeter = 0
    for side in nums:
        perimeter += side
    dict[perimeter] += 1

answer = 0
for k in dict.values():
    if k > answer:
        answer = k

for j in dict:
    if dict[j] == answer:
        print(j)

print(answer)
