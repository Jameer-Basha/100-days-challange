'''
In an array a superior element is one which is greater than all elements to its right. The rightmost element will always be considered as a superior element. You are given a function, static int FindNumberOfSuperiorElements(int[] arr)()

The function accepts an integer array 'arr' and its length 'n'. Implement the function to find and return the number of superior elements in array 'arr'.

Can you do this in O(n) time. That is in a single iteration.

Input Format

Input: arr: 7 9 5 2 8 7

Constraints

n>0

Array Index starts from 0.

Output Format

Sample Output: 3

Sample Input 0

7 9 5 2 8 7
Sample Output 0

3
Explanation 0

9 is greater than all the elements to its right,

8 is greater than all the elements to its right,

A per condition given, the rightmost element 7  be consider.

So {9,8, 7}: total '3 elements
'''

l=[int(x) for x in input().split()]

n=len(l)

c=1

for i in range(n-1):

    for j in range(i+1,n):

        if(l[i]<=l[j]):

            break

    else:

        c+=1

print(c)
