'''
Given an integer array and a number k, find the minimum unfairness. From the array pick up any k random integers. Their unfairness is defined as:

max - min in those k integers.

Use a function called unfairness that takes array and k as argument and returns the minimum unfairness as the answer.

Input Format

elements of array

k

Constraints

k<=n

Output Format

Integer denoting minimum unfairness.

Sample Input 0

10 20 100 200 300 30
3
Sample Output 0

20
Explanation 0

Here we have to choose 3 elements. If we choose 10 20 30 as the three elements, then max is 30 and min is 10. And max - min is 20. This is the minimum possible value of unfairness. The problem was to minimize the unfairness. So answer is 20

'''
l=[int(i) for i in input().split()]
k=int(input())
l.sort()
l1=[]
for i in range (len(l)-k+1):
    l1.append(l[k-1+i]-l[i])
print(min(l1))
