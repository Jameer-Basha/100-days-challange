'''
In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.

If it is, return the index of the largest element, otherwise return -1.

Example 1:

Input: nums = [3, 6, 1, 0]

Output: 1

Explanation: 6 is the largest integer, and for every other number in the array x, 6 is more than twice as big as x. The index of value 6 is 1, so we return 1.

Example 2:

Input: nums = [1, 2, 3, 4]

Output: -1

Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.

Note:

Input Format

5

1 2 2 3 7

Constraints

1 <= n <= 1000000000

Output Format

4

Sample Input 0

3
1 1 5
Sample Output 0

2
'''

n=int(input())
lst=list(map(int,input().split()))
Max=-1
for i in range(n):
    j=i+1
    
    for j in range(n):
        
        if(i!=j):
            #print(lst[i],lst[j])
            if(lst[i]<2*lst[j]):
                break
    if(j==len(lst)-1):
        Max= max(Max,i)
print(Max)
