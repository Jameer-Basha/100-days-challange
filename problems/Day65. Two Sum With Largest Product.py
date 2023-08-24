'''

Given an array and a number x, goal is to find the pair in the array with the sum equal to x, and the product should be maximum if there are multiple such pairs. For example, if arr is 6 10 12 11 15 3 and if x is 18, then (12 6) is one pair, (15 3) is another, but ans would be (12 6) This is standard pair sum problem. Start with an empty set. Check if target - curr is there in the set, not there, add element to the set. If it is there then see if prod is greater than max product and update your result. This problem should be done in O( n) time and not O(n^2) time.

Input Format

Array elements

Target

Constraints

Length of array is up to 10^5

Output Format

a b

where a>b and a+b = target.

Sample Input 0

6 10 12 11 15 3
18
Sample Output 0

12 6
Explanation 0

here 12 6 is the pair with sum = 18 and it has product of 72 which is greater than any other pair with sum 18


'''

b=int(input())
max1=0
for i in le:
    x=b-i
    if ((x in le) and (max1<(i*x))and(x>i)):
        y=x
        z=i
print(y,z)
