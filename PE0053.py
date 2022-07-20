#PE 53

def nCr(n, r):
	return fact(n) / (fact(r) * fact(n - r))

def fact(n):
	if(n == 0):
		return 1
	ret = 1
	for i in range(1, n+1):
		ret *= i
	return ret

if __name__ == "__main__":
	count = 0
	for n in range(1, 101):
		for r in range(n+1):
			if(nCr(n, r) > 1000000):
				count += 1

	print(count)