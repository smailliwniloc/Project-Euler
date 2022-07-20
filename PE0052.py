#PE 52

import collections

flag = False
n = 1
while(not flag):
	x1 = collections.Counter(str(n))
	x2 = collections.Counter(str(2*n))
	x3 = collections.Counter(str(3*n))
	x4 = collections.Counter(str(4*n))
	x5 = collections.Counter(str(5*n))
	x6 = collections.Counter(str(6*n))
	if(x1 == x2 and x2 == x3 and x3 == x4 and x4 == x5 and x5 == x6):
		flag = True
		print(n)
	n += 1
