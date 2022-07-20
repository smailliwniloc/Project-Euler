#PE 42

f = open("PE0042_words.txt")
a = f.read()

words = a.split(",")
for i in range(len(words)):
    words[i] = words[i][1:-1]

tri_nums = [int(.5*x*(x+1)) for x in range(100)]

answer = 0
for word in words:
    total = 0
    for letter in word:
        total += (ord(letter)-64)
    if total in tri_nums:
        answer += 1


print(answer)
