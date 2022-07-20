#PE 38

def conc_prod(x,n):
    string = ""
    for i in range(1,n+1):
        string += str(x*i)
    return string

pandigital = 0

for x in range(1,10000):
    for n in range(1,9):
        string = conc_prod(x,n)
        if len(string) == 9 and "1" in string and "2" in string and "3" in string and "4" in string and "5" in string and "6" in string and "7" in string and "8" in string and "9" in string and int(string) > pandigital:
            pandigital = int(string)

print(pandigital)
