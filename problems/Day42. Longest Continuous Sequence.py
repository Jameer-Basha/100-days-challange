'''
Given an array as input. Find the length of the longest continuous consecutive sequence that is present. For example: Let the array be:

7 9 15 3 18 2 25 19 17 14 16

Longest consecutive sequence is 14 15 16 17 18 19. So the answer should be 6.

You can get complexity of o(nlogn) using sorting. You can get complexity of O(n) using hashing. So the desired solution requires use of SET. DO NOT DO IT USING SORTING or brute force. USE SET.

Input Format

First line gives n, length of the array. Next line has n numbers.

Constraints

n<10^6

-10^9<=a[i]<=10^9

Output Format

Integer telling the length of longest consecutive sequence.

Sample Input 0

10
2 9 8 7 10 15 11 29 82 10
Sample Output 0

5
'''

n=int(input())
lst=list(set(map(int,input().split())))
lst.sort()
Longest=0
flag=1
count=0
for i in range(1,len(lst)):
    if (lst[i]-lst[i-1]==1):
        count+=1
    else:
        if(flag):
            Longest= max(Longest, count)
            count=0
Longest = max(Longest,count)
print(Longest+1)
