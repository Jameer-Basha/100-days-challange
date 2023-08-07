'''
Given an input of a sequence of numbers. Find the longest sequence that can be expressed as a mxn matrix with n>=m and which has all numbers from 1 to m*n. Print all such matrices in the output. If no such matrix exists, print -1. Given m,n<4, that is both m and n will be up to maximum of 3.

For example:

21,1,3,7,6,5,4,2,1,3,5,6,9,8,7,2,4,1

The output should be:

4 2 1

3 5 6

9 8 7

1 3 5

6 9 8

7 2 4

3 5 6

9 8 7

2 4 1

There are three such matrices with length 9. If we had no such matrix of length 9, we would have searched for matrix with length, 6 and then 4 and then 2, where n is greater than m. Remember if it is a 2x3 matrix, it must have numbers from 1 to 6.

Input Format

Read sequence of numbers

Output Format

Display the matrices

Sample Input 0

21 1 3 7 6 5 4 2 1 3 5 6 9 8 7 2 4 1
Sample Output 0

4 2 1
3 5 6
9 8 7
1 3 5
6 9 8
7 2 4
3 5 6
9 8 7
2 4 1
Sample Input 1

21 1 3 7 6 5 4 2 1 3 5 6 9 8 7 3 3 1
Sample Output 1

4 2 1
3 5 6
9 8 7


'''

s = list(map(int,input().split()))

def Possible(input_lst,long):
    res=[]
    lst=[]
    if(long==9 or long==6 or long ==3):
        sub=3
    elif(long==1):
        sub=1
    else:
        sub=2 
    for i in range(len(input_lst)):
        s= input_lst[i:i+long]
        
        if(len(s)<long):
            break
        
        if(check(s,long)):
            #print(long)
            for k in range(long):  
                lst.append(s[k])
                if(len(lst)==sub):
                    res.append(lst)
                    lst=[]
    return res

def check(s,n):
    for i in range(1,n+1):
        if i not in s:
            return False
    return True

res=Possible(s,9)
if(len(res)==0):
    res=Possible(s,6)
    if(len(res)==0):
        res=Possible(s,4)
        if(len(res)==0):
            res= Possible(s,3)
            if(len(res)==0):
                res=Possible(s,2)
                if(len(res)==0):
                    res=Possible(s,1)
    
if(len(res)==0):
    print(-1)
else:
    for i in res:
        ans =" ".join(str(j) for j in i)
        print(ans)
            
