'''
Problem statement
You are given a function,
int FindLongestSubstring(char• s, int n);
The function accepts a strtng 's' of length n. The string 's' consists
of digits varying from 0-9. Implement a function to find longest
even length substring of string such that the length of the
substring is 2k digits and sum of left k digits is equal to the sum of
right k digits and return the length of the substring found.
Note : Return O if no such substring is possible with given
condition.
'''
n =input()
res=[]
def sumOfDigits(n):
    if n=="":
        return 0
    sum=0
    n=int(n)
    while(n>0):
        rem=n%10
        sum+=rem
        n=n//10
    return sum
def longestEvenString(sub):
    Max=0
    n=len(sub)
    if n%2!=0:
        return 0
    right=sub[:n//2]
    left= sub[n//2:]
   
    if(sumOfDigits(right)==sumOfDigits(left)):
        Max=n
    return Max
for i in range(len(n)):
    for j in range(i+1,len(n)+1):
        sub = n[i:j]
        res.append(longestEvenString(sub))
print(max(res))
