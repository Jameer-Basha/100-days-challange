'''

Given a string with all small English alphabets, two numbers p and k. Find the min Grade that can come at position p after a maximum of k swaps. Goal is to minimize the letter at position p. Start with 1 indexing.

Input Format

String

p

k

Constraints

none

Output Format

-

Sample Input 0

dsfhsdklfhasdlkhfsdhfjksdhf
4
2
Sample Output 0

d
Explanation 0

Within two swaps we can get the next d at the position of h, the 4th position.


'''

s=input()
p=int(input())
k=int(input())
left =p-k
if(left<1):
    left=1
right =p+k
if(right>len(s)):
    right=len(s)
sub=s[left-1:right]
print(min(sub))
