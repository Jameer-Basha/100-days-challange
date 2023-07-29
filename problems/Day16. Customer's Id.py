'''
The e-commerce company "BuySellGoods" processes its customer orders through order id. The order id is generated automatically by their system with the help of the customer id. The order id can be positive or a negative number. The negative order id denotes the cancelled order by the customer. The company system takes the customer id as the first term and a common ratio R. The order id is the Nth term in the geometric progression of the series.

Write an algorithm to generate the customer's order id.

Input Format

The input consists of three space seperated integers - customerId, cmnRatio, term represnting the customer ID, the common ratio of the series(R) and the Nth term of the GP.

Constraints

-10^6 <= customerId <= 10^6 -10^6 <= cmnRatio <= 10^6 0 < terms <= 10^6

Output Format

Print an integer represnting the order id.

Sample Input 0

3 2 4
Sample Output 0

24
Explanation 0

Customer_id = 3 Common Ratio = 2 Nth term = 4

having values a = 3, r = 2, n = 4 By Geometric Progression,

a.r^n-1 = 3.2^(4-1) = 24

'''
n,k,m = map(int,input().split())
print(n*k**(m-1))
