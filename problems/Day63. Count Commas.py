'''
Given a number N, we have to find that while writing all numbers from 1 to N, how many commas will be used. After every three digits a comma is used. Thus, 1,000 is correct. Similarly 51,000,000,000 is the correct representation. Similarly 1,455,343 is correct. So given N output how many commas will be used from 1 to N.

Input Format

N

Constraints

N<=10^18

Output Format

Number of commas used.

Sample Input 0

1010
Sample Output 0

11
Explanation 0

Commas will start from 1000 onwards. So total 11 commas are required.

'''

n=int(input())
digits=len(str(n))
commas = (digits-1)//3
res=0
while n>999:
    lower = 10** (commas*3)
    res+=(n-lower+1)*commas
    n =lower-1
    digits = len(str(n))
    commas= (digits-1)//3
print(res)
