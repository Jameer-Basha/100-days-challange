'''
Given a string with just numbers and operators +,-,*,/. Calculate the value of the equation. Remember * and / have higher precedence, so they should be computed first. If two operators come of the same precedence, then evaluate from left to right. Use only Integeral calculations. So 5/2 is 2 and 1/2 is 0.

Input Format

String input

Constraints

-

Output Format

Integeral value after computation

Sample Input 0

10+51/2*2-3
Sample Output 0

57
Explanation 0

First compute 51/2 that is 25. Then it becomes 50, and then 10 are added and 3 is subtracted. So the final value is 57

Sample Input 1

-10+51/2*2-3
Sample Output 1

37
Explanation 1

Calculation is obvious.


'''

expression =input()
expression= expression.replace('/','//')
print(eval(expression))
