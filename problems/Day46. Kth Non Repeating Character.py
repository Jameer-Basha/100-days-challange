'''

Find k’th non-repeating character in the string while traversing string from left to right.

Input Format

First line contains string and second line contains integer k.

Constraints

1<= string length <= 10^6

1<=k<=26

Output Format

Print the k’th non repeating character in the string if it exists or if it does not exist then print -1.

Sample Input 0

popcorn
2
Sample Output 0

r
Explanation 0

c is first non repeating string, and r is second one.

Sample Input 1

aaaaaaaaaaaaaaaaaaaaaa
3
Sample Output 1

-1

'''

s=input()
k=int(input())
res=[]
for i in s:
    if s.count(i)==1:
        res.append(i)
    if(len(res)>=k):
        break
        
if(len(res)<k):
    print(-1)
else:
    print(res[-1])
    
