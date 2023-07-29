'''
Given a number N and another number K, find the last digit of the number formed when N is raised to the power K.

Note:the values of N and K can be very large.

Input Format

input1: The Number N input2: The Number K.

Constraints

_

Output Format

Return the last digit of the number formed when input1 is raised to the power of input2.

Sample Input 0

3333333333333333333333222222222222222222226
2899999999999999999444444444444444444444444444444
Sample Output 0

6
Explanation 0

Any power of 6 always ends up in a 6.

Sample Input 1

4237777777777777777777777777777
10000
Sample Output 1

1
Explanation 1

Any power of 7 can end with 7^1 = 7

7^2 = 49 last digit 9

7^3 = last digit 3

7^4 = last digit 1

and then it repeats.

Here 1000%4 is 2. Hence we have the same last digit as 7^2

'''

n=int(input())
k=int(input())
last = str(n)[-1]
rem = k%4
if(rem==0):
    rem=4
pow = str(int(last)**rem)[-1]
print(pow)
