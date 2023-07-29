'''
In a premier championship series o(sports car
racing,iåtially, the IS car is aheacjOf the 2n car by
X After that. in every ?eCond, the IS car
@ves ahead by nl metres and the 2nd car moves
Ghead by n2 metres (in the same direction). The task
nd
is to print the number of seconds after which the 2
car crosses the ISt car. If it is impossible to do so,
then print -1.

'''
n1 = int(input())
n2 = int(input())
X= int(input())
first =X
second =0
count=0
if(n1>=n2):
    print(-1)
else:
    while(second<=first):
        first+=n1
        second+=n2
        count+=1
    print(count)
