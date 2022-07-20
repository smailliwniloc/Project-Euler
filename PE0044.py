#PE 44

pentagonals = [int(.5*n*(3*n - 1)) for n in range(1,5000)]


done = False
for a in range(len(pentagonals)):
    for b in pentagonals[a:]:
        if pentagonals[a]+b in pentagonals and b-pentagonals[a] in pentagonals:
            print(b-pentagonals[a])
            done = True
            break
    if done:
        break
