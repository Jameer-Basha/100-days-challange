'''
Given a row/column count and a matrix, your job is to find those possible 2*2 matrix where each should follow the given rule :

-> Each element of matrix should be divisible by sum of its digits.

Input :

First Input : Row count

Second Input : Matrix

Output :

2*2 matrices satisfying the rule.

Input Format

First line contains Row count Second line read matrix

Constraints

None

Output Format

display 2*2 matrix according above criteria values are comma separated.

Sample Input 0

4
40,42,2
30,24,27
180,190,40
11,121,13
Sample Output 0

40,42
30,24
42,2
24,27
30,24
180,190
24,27
190,40


'''

n=int(input())
lst=[]
res=[]
for i in range(n):
    lst.append(list(map(int,input().split(","))))
    
def sumOfDigits(num):
    Sum=0
    while(num>0):
        Sum+=num%10
        num=num//10
    return Sum

def Possible():
    possible=[]
    
    for i in range(n-1):
        for j in range(len(lst[0])-1):
            new1=""
            new2=""
            n1=lst[i][j]
            n2=lst[i][j+1]
            n3=lst[i+1][j]
            n4=lst[i+1][j+1]
            if (n1%sumOfDigits(n1)==0 and n2%sumOfDigits(n2)==0 and n3%sumOfDigits(n3)==0 and n4%sumOfDigits(n4)==0):
                new1+=str(n1)
                new1+=","
                new1+=str(n2)
                new2+=str(n3)
                new2+=","
                new2+=str(n4)
                
                possible.append(new1)
                possible.append(new2)
    return possible

res = Possible()
if(len(res)>0):
    for i in res:
        print(i)
else:
    print(-1)
