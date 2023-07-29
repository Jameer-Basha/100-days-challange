'''
Implement the following function:

int DiffMinPrimeFactor(int n);

The function accepts an integer 'n'. Implement the function to find the minimum prime factor of 'n' and return difference of 'n' with its minimum prime factor.

Prime factors: The prime numbers that divides an integer exactly are called its prime factors.

Input Format

Sample Input: n: 350

Constraints

n > 1
1 is not a prime number
Output Format

Sample Output: 348

Sample Input 0

350
Sample Output 0

348
Explanation 0

350 = 2 x 5 x 5 x 7 , [Prime Factors of 350]

Minimum prime factor of 350, is 2

Difference = 350 - 2 = 348.

'''

n= int(input())
def isPrime(num):
    root = int(num**0.5)
    for i in range(2,root+1):
        if num%i==0:
            return False
    return True

def minPrimeFactor(n):
    root = int(n**0.5)
    ans=n
    for i in range(2,root+1):
        if isPrime(i):
            if n%i==0:
                ans=i
                break
    return ans

print(n-minPrimeFactor(n))
