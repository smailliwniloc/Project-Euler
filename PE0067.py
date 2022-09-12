#PE 67

def openTriangle(path):
    tri_file = open(path)
    lines = tri_file.read().split("\n")

    return [[int(x) for x in row.split()] for row in lines]

def maxSum(triangle, i=-1):
    if -i == len(triangle):
        return triangle[0][0]
    for j in range(len(triangle[i]) - 1):
        M = max(triangle[i][j], triangle[i][j+1])
        triangle[i-1][j] += M
    return maxSum(triangle, i-1)

if(__name__ == "__main__"):
    triangle = openTriangle("PE0067_triangle.txt")
    print(maxSum(triangle))
    