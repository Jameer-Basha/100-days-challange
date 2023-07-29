'''
Given an array of size N, Interchange the kth element from beginning with kth element from end.

Input Format

INPUT:

N = 5, K = 2

Arr[] = {5, 3, 6, 1, 2}

Constraints

_

Output Format

OUTPUT:

5 1 6 3 2

Sample Input 0

8
3
1 2 3 4 5 6 7 8
Sample Output 0

1 2 6 4 5 3 7 8

'''
n=int(input())
k=int(input())
lst =list(map(int,input().split()))
front=lst[k-1]
back=lst[-k]
lst[k-1]= back
lst[-k]= front
res =" ".join(str(i) for i in lst)
print(res)
