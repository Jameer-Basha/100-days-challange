'''
Given an array arr[] of integers, find out the maximum difference between any two elements such that larger element appears after the smaller number.

Input : arr = {2, 3, 10, 6, 4, 8, 1} Output : 8 Explanation : The maximum difference is between 10 and 2.

Input : arr = {7, 9, 5, 6, 3, 2} Output : 2 Explanation : The maximum difference is between 9 and 7. Think what will happen if all elements are equal. If there is no such pair then print -1. In case we have two equal elements and no other value satisfying the given criteria, answer should be 0.

Input Format

n elements in line

Constraints

All are Integers

Output Format

maximum difference

Sample Input 0

2 3 10 6 4 8 1
Sample Output 0

8


'''
l=list(map(int,input().split()))

m=0

k=l[0]

for i in range(1,len(l)):

    if(l[i]>=k):

        m=max(m,l[i]-k)

    k=min(k,l[i])

if((l[0] in l[1::]) and m==0):

    print(0)

elif(m==0):

    print(-1)

else:

    print(m)
