'''


Find the greatest product of k consecutive digits in the N digit number.

Input Format

First line contains T that denotes the number of test cases.
First line of each test case will contain two integers N & K.
Second line of each test case will contain a N digit integer.

Output Format

Print the required answer for each test case.

Sample Input 0

2
10 5
3675356291
10 5
2709360626
Sample Output 0

3150
0
Explanation 0

For 3675356291 and selecting K=5 consequetive digits, we have 36753, 67535, 75356, 53562, 35629 and 56291. Where  6x7x5x3x5 gives maximum product as 3150
For 2709360626, 0 lies in all selection of 5 consequetive digits hence maximum product remains 0


'''

def productOfdigits(n):
    n=int(n)
    pro=1
    while(n>0):
        pro*= n%10
        n=n//10
    return pro

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    
    max_pro=0
    for i in range(n-k-1):
        sub = num[i:i+k]
        pro=productOfdigits(sub)
        if(pro>max_pro):
            max_pro=pro
    print(max_pro)
