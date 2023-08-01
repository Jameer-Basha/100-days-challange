'''
Sample Input 0

34,89,6,321,53,45,2211,81
Sample Output 0

4
Explanation 0

Here the following four pairs have the same sum of digits. - 6 and 321 - 6 2211 - 321 2211 - 45 81
'''


lst=list(set(map(int,input().split(","))))

def sumOfDigits(num):
    Sum=0
    while(num>0):
        Sum+=num%10
        num= num//10
    return Sum

Sum_lst=[]
for i in lst:
    Sum_lst.append(sumOfDigits(i))
Final_count =0
Set = list(set(Sum_lst))
for i in Set:
    Count = Sum_lst.count(i)
    if(Count>1):
        Final_count += (Count*(Count-1))//2
if(Final_count>0):
    print(Final_count)
else:
    print(-1)
