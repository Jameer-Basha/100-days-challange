'''

Write a function longest_common_substring that takes two strings word1 and word2 and returns the maximum overlap between the strings.

Sample Input ...................... Expected Output
pirate, teepee ..................... te
fish, bowl ........................... -1
assured, measured................... sured
catenation, concatenation ................... catenation

The overlap must be of two chars at least, otherwise print -1

If multiple overlaps of the same length, then print the one that appears first in the first string.

Input Format

Two strings

Constraints

None

Output Format

Longest common substring

Sample Input 0

pirate
teepee

Sample Output 0
te
'''
s1=input()
s2=input()
Longest =""
if(len(s2)>len(s1)):
    s1,s2=s2,s1
    
def isValid(string):
    
    return string in s1

for i in range(len(s2)):
    for j in range(i+1,len(s2)+1):
        string=s2[i:j]
        if(isValid(string)):
            if(len(string)>len(Longest)):
                   Longest=string
if(Longest==""):
    print(-1)
else:
    print(Longest) 
