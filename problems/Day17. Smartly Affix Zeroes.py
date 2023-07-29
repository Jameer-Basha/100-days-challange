'''
Given a pair of positive integers m and n, m < n, write a program to smartly affix zeroes while writing numbers from m to n.

Input Format

Single line with m and n

Constraints

0

Output Format

Print all numbers from m to n in a single line, all numbers should have same number of digits with prefixed zeroes if required.

Sample Input 0

5 10
Sample Output 0

05 06 07 08 09 10
Sample Input 1

1 9
Sample Output 1

1 2 3 4 5 6 7 8 9


'''
first,last = map(int,input().split())
length = len(str(last))
for i in range(first,last+1):
    i = str(i)
    res = i.zfill(length)
    print(res, end =" ")
