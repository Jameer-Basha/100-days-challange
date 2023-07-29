'''
Given a square matrix, calculate the absolute difference between the sums of its diagonals
'''
def diagonalDifference(arr):
    # Write your code here
    d1=0
    d2=0
    n=len(arr)
    for i in range(n):
        d1+= arr[i][i]
        d2+=arr[i][n-i-1]
    return abs(d1-d2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
