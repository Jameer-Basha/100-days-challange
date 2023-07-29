'''
Consider a non-empty string instr consisting of mer case alphabets
ONLY. Identify and print outarr based on the following logic:
• Identity all the unique balanced substrings that can be formed using
instr and add them to outarr in the increasing order of their lengttl
o A balanced substring is one where ALL the characters of the
substring can be partitioned into two groups GI and G2 such
that
• If two or more balanced substrings have the same length, add them to
outarr in alphabetical order
• Print -1, if no balanced substnng can be formed using instr
Input format:
First line contains instr
Read the input from the standard input stream.
Output format:
Pont outarr with elements separated by '(comma) or •1 accordingly to the
standard output stream
'''

n=input()
length = len(n)
res =[]

def isBalanced(sub):
    if len(sub)%2 != 0:
        return False
    for i in sub:
        if sub.count(i)%2!=0:
            return False
    return True

for i in range(length):
    for j in range(i+1, length+1):
        sub = n[i:j]
        if (sub not in res and isBalanced(sub)):
            res.append(sub)
if(len(res)>0):
    sort_key = lambda s: (len(s), s)
    res.sort(key = sort_key)
    ans = ",".join(i for i in res)
    print(ans)
else:
    print(-1)
