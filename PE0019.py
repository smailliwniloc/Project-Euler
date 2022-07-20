#PE 19
#Monday is 1 mod 7, Tuesday is 2 mod 7, ..., Sunday is 0 mod 7

year = 1900
day = 1
month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
sundays = 0

while year < 2001:
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                month_days[1] = 29
            else:
                month_days[1] = 28
        else:
            month_days[1] = 29
    else:
        month_days[1] = 28
    for month in month_days:
        day += month
        if day%7 == 0 and year > 1900:
            sundays += 1
    year += 1

print(sundays)
