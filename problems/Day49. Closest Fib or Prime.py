'''

Given a number n, find the number starting from n which is either prime or Fibonacci. The first such number that is either prime or Fibonacci is the answer.

Hint: Write two functions isFibo and isPrime. Starting from n keep on checking till you find a number that is either Fib or prime.

Prime numbers are 2 3 5 7 11 etc.

Fib numbers are 0 1 1 2 3 5 8 13 etc.

For example: Input

10

Output

11

Input

34

Output

34

Input Format

Number n

Constraints

n is less than 100000

Output Format

Number that is prime or in Fibonacci series.

Sample Input 0

10
Sample Output 0

11
Sample Input 1

34
Sample Output 1

34

'''
n=int(input())

def isPrime(num):
    if(num<=1):
        
        return False
    root =int(num**0.5)
    for i in range(2,root+1):
        if(num%i==0):
            return False
    return True

def isFib(num):
    if(n==0 or n==1):
        return True
    first=0
    second=1
    while(second<=n):
        next=first+second
        first,second=second,next
        if(second==n):
            return True
    return False
    
while(True):
    if(isFib(n) or isPrime(n)):
        print(n)
        break
    else:
        n=n+1
