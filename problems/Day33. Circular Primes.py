'''
The number,197 , is called a circular prime because all rotations of the digits: ,971 ,719 and ,197 are themselves prime.

There are thirteen such primes below 100

Find the sum of circular primes that are below ?

Note
Rotations can exceed .

Input Format

Input contains an integer 

Constraints

Output Format

Print the answer corresponding to the test case.

Sample Input

100
Sample Output

446
'''
n=int(input())
circular_primes=[2,3,5,7,11,13,17,31,37,71,73,79,97]

def isPrime(num):
    root =int(num**0.5)
    for i in range(2,root+1):
        if num%i==0:
            return False
    return True

def isCircularPrime(num):
    string = str(num)
    string=string[1:]+string[:1]
    while(string != str(num)):
        if(not isPrime(int(string))):
            return False
        string=string[1:]+string[:1]
    return True


if(n>100):
    for i in range(101,n+1):
        if (isPrime(i)):
            if(isCircularPrime(i)):
                circular_primes.append(i)
    print(sum(circular_primes))
else :
    sum=0
    for i in circular_primes:
       if(i<=n):
          sum+=i
    print(sum)
