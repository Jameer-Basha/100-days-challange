'''

Given a string, no.of queries and quenry list
query is either 1 or 2
if query is 1 you need to swap first and last charcter of a string
i query is 2 you need to swap first half wth last half

'''

def swapString(input1,input2,input3):
  length = len(input1)
  s=list(input1)
  k = length - length//2
  for i in input3:
    if i ==1:
      s[0],s[-1]=s[-1],s[0]
    if i==2:
      s[:length//2],s[k:]= s[k:],s[:length//2]
  res ="".join(s)
  return res

s=input()
n=int(input())
lst =list(map(int,input().split()))
print(swapString(s,n,lst))
