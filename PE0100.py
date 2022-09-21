# PE 100

# Solving Diophantine Equation via https://www.alpertron.com.ar/QUAD.HTM gave this recurrence

blue, n, L = 1, 1, 10**12
while n <= L:
    blue, n = 3*blue + 2*n - 2, 4*blue + 3*n - 3

print("Number of Blue disks, number of total disks =", blue, n)