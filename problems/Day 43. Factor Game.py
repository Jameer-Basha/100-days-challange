'''
For a given list of numbers, find its factors and add the factors. Then add all the numbers whose sum of factors is present in the original list to the result list, sort the result list and print it else print -1.

Input :

First Input : List of numbers

Output : List of numbers whose sum of factors is there in the original list in sorted order.

Input Format

Read List of Numbers

Constraints

Each number can be of upto 12 digits. (So do not think of a for loop upto n/2 to get all the factors. Go only up to sqrt(n))

Output Format

Numbers whose sum of factors is there in the list in sorted order.

Sample Input 0

7 4 1 2
Sample Output 0

1 4
Explanation 0

Here factors of 1 are only 1 and 1 is there in the list. Factors of 2 are 1 and 2 and the sum is 3, but 3 is not in the list. Factors of 4 are 1 2 and 4 and sum is 7, and 7 is there in the list so 4 is printed. Factors of 7 are 1 and 7, 8 is not there in the list. So not printed.

Sample Input 1

2 4
Sample Output 1

-1

'''
lst =list(map(int,input().split()))
lst.sort()
def factorsSum(num):
    Sum=0
    root= int(num**0.5)
    for i in range(1,root+1):
        if(num%i==0):
            Quotient = num//i
            if(Quotient != i):
                Sum+=Quotient
            Sum+=i
    
    return Sum

Max =max(lst)
res=[]
Max_root = int(Max**0.5)
for i in lst:
    Factors = factorsSum(i)
    
    if(Factors in lst):
        res.append(i)
        
if(len(res)>0):
    ans =" ".join(str(i) for i in res)
    print(ans)
else:
    print(-1)
            
