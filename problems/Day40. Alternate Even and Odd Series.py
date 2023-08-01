'''
Write a program for printing Alternate even odd series.

input:- A5w8@k7!123n69

output:-85276139

If number of special character in the given string is even so we should print first evendigits and next odd digits alternate in the same series as they present in the string

input:-#bn7856!@kn2n65jbnj482375

output:-7856523674582

If number of special characters in the given string is odd so we should first print odd digit and then even digit alternate in the same series as they present in the string

Input Format

Read a string with special cahracters and numbers

Constraints

None

Output Format

display the resultant sequence

Sample Input 0

A5w8@k7!123n69
Sample Output 0

85276139
Sample Input 1

#bn7856!@kn2n65jbnj482375
Sample Output 1

7856523674582

'''

s=input()
even=[]
odd=[]
count=0
for i in s:
    if(i.isdigit()):      
        i=int(i)
        if(i%2==0):
            even.append(i)
        else:
            odd.append(i)
    elif(not i.isalpha()):
        count+=1
            
if(count%2==0):
    start=0
else:
    start=1
    
odd_index=len(odd)
even_index=len(even)
max_index=max(odd_index,even_index)

ans=""
for i in range(max_index):
    if(not start):
        if(i<even_index):
            ans+=str(even[i])
        if(i<odd_index):
            ans+=str(odd[i])
    if(start):
        if(i<odd_index):
            ans+=str(odd[i])
        if(i<even_index):
            ans+=str(even[i])
        
print(ans)
