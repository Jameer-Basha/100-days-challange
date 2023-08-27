'''
You are given three integers a,b,c you have to 4 digit generate ATM pin based on the following condintions
i) Thousands place of ATM pin is a Biggest number with Maxinmum Frequency
ii) Hundreds place is Smallest number with frequency =1
iii) In Tens Place is Biggest digit in all three numbers
iv) In Ones place is Smallest digit in all three numbers.

Example:

Input:
1234
3456
5678

output: 6181

Explaination: 3,4,5,6 are having frequency 2 . Among them 6 is biggest so thousands place is 6
1,2,7,8 are repated 1 time . smallest number 1 is hundreds place
8 is biggest digit among all the numbers and 1 is smallest

'''

a=input()
b=input()
c=input()
s= a+b+c
lst=list(s)
sett=set(lst)
Max_count_lst=[]
Non_rep_lst=[]
Max_count=1

for i in sett:
    cnt =lst.count(i)
    if(cnt>Max_count):
        Max_count =cnt
        Max_count_lst=[i]
    elif(cnt == Max_count):
        Max_count_lst.append(i)
    if(cnt==1):
        Non_rep_lst.append(i)
print(max(Max_count_lst)+min(Non_rep_lst)+max(lst)+min(lst))
