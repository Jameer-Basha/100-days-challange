'''
Given an array and multiple occurances of two integers x and y, find the minimum number of elements between x and y in the array.

Input Format

First line: array elements

Second line: x and y

Constraints

if x or y or both are not there in the array, return -1.

Output Format

an Integer representing minimum number of elements between x and y

Sample Input 0

17 4 7 2 9 16 12 9 8 3 4 6 3 9 10 4 8 8 2 4
4 9
Sample Output 0

1
Explanation 0

Here 4 and 9 come several times in the array. First time 4 7 2 9, they have two elements in between them. But when 9 10 4 comes, they have only one element between them. So minimum value is 1.

'''
lst = list(map(int,input().split()))
start,end = map(int,input().split())

def minInteger():
    if start not in lst or end not in lst:
        return -1
    
    n =len(lst)
    minn = n
    minDiff=n
    start_index=0
    end_index=n-1
    
    for i in range(n):
        if(lst[i] == start):
            start_index=i
        elif(lst[i]==end):
            end_index=i
        if(start_index!=0):
            minDiff= abs(start_index-end_index)
        
        minn =min(minn,minDiff)
    return minn-1

print(minInteger())
            
        
