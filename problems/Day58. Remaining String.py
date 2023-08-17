'''
Given a string with only English alphabets, for each alphabet print how many more of the same alphabets are to its right.

For example if the input is: abaa

Output should be

2 0 1 0

because for first a there are two more a's, but for b there is no more b, then for next a there is one more a and for last a there is nothing.

Input Format

string with English alphabets

Constraints

length|string|<=10^5

Output Format

for each location print how many same alphabets are after it.

Sample Input 0

abbaa
Sample Output 0

2 1 0 1 0
Explanation 0

After first a there are two more a's

After first b there is one more b

After second b there is no more b

After second a there is one more a

After last a there is no more a.
'''

s=input()
length = len(s)
res=[]
for i in range(length):
    sub = s[i+1:]
    #print(sub)
    cnt =sub.count(s[i])
    res.append(cnt)
ans = " ".join(str(i) for i in res)
print(ans)
