'''
Consider a non-empty array inarr containing N positive integers and consider a positive integer innum, Print a number outnum number of unique integers left in inarr after innum number of removals. Goal is to minimize the output.

Input Format:

First line contains the number innum, that is the number of elements that have to be removed.

Second line contains the array of inegers inarr,with the elements separated by space

Read the inputs from the standard input stream

Output Format:

Print outnum to the standard output stream

Eliminate the numbers with minimum frequency first so that you get minimum unique numbers. Goal is to minimize the unique numbers.

Input Format

First line contains number innum Second line contains array of integers inarr

Constraints

where 0

Output Format

Print outnum to the standard output stream

Sample Input 0

2
1 2 3 3
Sample Output 0

1
Explanation 0

we can make two removals, so if we remove 1 and 2, only unique number remaining is 3. So ans is only 1.

Sample Input 1

3
1 2 5 6 6 5
Sample Output 1

2

'''
n=int(input())
lst = list(map(int,input().split()))
res =[]
sett =list(set(lst))
for i in sett:
    res.append(lst.count(i))
res.sort()
count=0
while (n>0):
    n -= res[0]
    if(n<0):
        count=1
    res.pop(0)
print(len(res)+count)
