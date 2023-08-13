'''
Infinite number of people are crossing a 2-D plane. They march in such a way that each integral x coordinate has only one person who moves parallel to the y axis and starting from (x,0). You have barriers placed represeneted by a barrier matrix. The matrix has N rows and 3 columns. Each column has three values (x,y,d). It represents a barrier that starts from (x,y) and goes up to (x+d,y). Once a person encounters a barrier he stops moving. Given the barrier matrix, you have to find out how many people stopped moving.

Input Format

A n * 3 matrix representing the barriers. Each row has a barrier placed from (x,y) to (x+d,y)

Constraints

DO NOT USE EXTRA MEMORY.

Output Format

Total number of people stopped. Note the barriers may overlap

Sample Input 0

2
2 3 3
4 6 4
Sample Output 0

7
Explanation 0

First barrier is from 2 till 5. Second one is from 4 till 8. So effectively there is a barrier from 2 till 8, that is total of 7 people from 2,3,4,5,6,7,8 will be blocked.

Note here the final barrier need not be continous. For example if we had barrier from 2 to 4 and another barrier from 6 to 10, then 8 people would have been stopped.

'''


def MaximumBarrier(barrier):
    res=[]
    for i in barrier:
        start=i[0]
        distance=i[2]
        res.append((start,start+distance))
    last=0
    res.sort()
    count=0
    for vals in res:
        if(vals[0]>last):
            count+=vals[1]-vals[0]+1
            last=vals[1]
        elif(vals[1]>last):
            count+=vals[1]-last
            last=vals[1]
    return count
n=int(input())
res=[]
for i in range(n):
    lst=list(map(int,input().split()))
    res.append(lst)
print(MaximumBarrier(res))
