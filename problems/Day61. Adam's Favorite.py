'''

Given two inputs l and x, find number of Pairs (a,b) where 1<=a<=b<=l and GCD(a,b) = x.

Input Format

l x

Constraints

l <=10^4

Output Format

Give the number of pairs satisfying the above condition.

Sample Input 0

5 3
Sample Output 0

1
Explanation 0

There is only one pair 3,3 what satisfies GCD = 3

'''


i,x = map(int,input().split())
cnt =0

def gcd(a,b):
    if(b==0):
        return a
    return gcd(b,a%b)

for k in range(x,i+1):
    for j in range(k, i+1):
        if(gcd(k,j) == x):
            cnt+=1
print(cnt)
