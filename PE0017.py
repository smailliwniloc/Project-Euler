#PE 17

spellings = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen", 20:"twenty",
                30:"thirty", 40:"forty", 50:"fifty", 60:"sixty", 70:"seventy", 80:"eighty", 90:"ninety", 100:"onehundred", 200:"twohundred", 300:"threehundred", 400:"fourhundred", 500:"fivehundred", 600:"sixhundred", 700:"sevenhundred", 800:"eighthundred",900:"ninehundred",1000:"onethousand"}
total = 0
for i in range(1,1001):
    x = str(i)
    if i%10 == i:
        total += len(spellings[i])
    elif i%100 == i:
        x1 = int(x[0])
        x2 = int(x[1])
        if x1 == 1:
            total += len(spellings[i])
        elif x2 == 0:
            total += len(spellings[i])
        else:
            total += len(spellings[10*x1]) + len(spellings[x2])
    elif i%1000 == i:
        x1 = int(x[0])
        x2 = int(x[1])
        x3 = int(x[2])
        if x2 == 0 and x3 == 0:
            total += len(spellings[i])
        elif x2 == 0:
            total += len(spellings[100*x1]) + len(spellings[x3]) + 3
        elif x3 == 0:
            total += len(spellings[100*x1]) + len(spellings[10*x2]) + 3
        elif x2 == 1:
            total += len(spellings[100*x1]) + len(spellings[i%100]) + 3
        else:
            total += len(spellings[100*x1]) + len(spellings[10*x2]) + len(spellings[x3]) + 3
    else:
        total += len(spellings[1000])

print(total)
