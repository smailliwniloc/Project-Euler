#PE 6
sum_of_squares = 0
for i in range(1,101):
    sum_of_squares += i**2

print("sum of squares is {}".format(sum_of_squares))

summ = 0
for i in range(1,101):
    summ += i
square_of_sum = summ**2

print("square of the sum is {}".format(square_of_sum))

difference = square_of_sum - sum_of_squares

print("the difference is {}".format(difference))
