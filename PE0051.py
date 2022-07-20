#PE 51

def Sieve(n):
	prime = [True for i in range(n+1)]
	p = 2
	while(p*p < n):
		if(prime[p]):
			for i in range(p*2, n+1, p):
				prime[i] = False
		p+=1
	prime[0] = False
	prime[1] = False
	primes = []
	for i in range(len(prime)):
		if(prime[i]):
			primes.append(i)
	return primes

def Permutations(n):
	perms = [str(bin(i))[2:] for i in range(n+1)]
	return perms

if __name__ == "__main__":
	N = 1000000
	primes = Sieve(N)
	low = 100000
	perms = Permutations(63)[32:]
	#searching through all primes
	for p in primes:
		#only 6 digits numbers
		if(p > low):
			
			#looking through all permutations to change digits in 
			for perm in perms:

				count = 0
				fails = 0
				num = '0'
				while(count < 8 and fails < 3):
					tester = str(p)
					#change tester to match permutation with num
					for i in range(len(perm)):
						if(perm[i] == '1'):
							s = list(tester)
							s[i] = num
							tester = "".join(s)
					#see if the new number is prime
					if int(tester) in primes:
						count += 1
						#print(tester + ": " + str(count))
					else:
						fails += 1
						#print("fails = " + str(fails))
					num = str(int(num) + 1)
					#print("finished on " + tester)
					if(count == 8):
						print(p)
						print(perm)





	