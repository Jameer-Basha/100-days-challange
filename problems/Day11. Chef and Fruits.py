'''
Question 11:

Chef and Fruits

Today is Deekshith's birthday. His mom has surprised him with truly fruity gifts: 2 fruit baskets. The first basket contains N apples, and the second one contains M oranges. Deekshith likes apples and oranges very much but he likes them equally, and therefore, wants to have the minimum possible difference between the number of apples and oranges he has. To do so, he can purchase 1 apple or 1 orange by paying exactly 1 gold coin (that's some expensive fruit, eh?). Deekshith can purchase fruits at most K times (as he has only K gold coins in his pocket) to make the difference the minimum possible.

Deekshith is busy in celebrating his birthday to the fullest, and therefore, he has handed this job to his best friend — you. Can you help him by finding the minimum possible difference he can achieve between the number of apples and orange he owns?

Input Format

The first line of input contains a single integer T denoting the number of test cases. The first and only line of each test case contains 3 space separated integers — N, M and K — denoting the number of apples, number of oranges, and number of gold coins Deekshith has.

Output Format

For each test case, output the minimum possible 
difference between the number of apples and oranges that Chef can achieve.

Constraints

1 ≤ T ≤ 100
1 ≤ N, M, K ≤ 100

Example1 :

Input :
Test cases :  3 
Test case1 :3 4 1 
Test case2: 5 2 1 
Test case3: 3 4 3

Output :
0 
2 
0

Explanation:
Test 1: Chef will buy 1 apple by paying 1 gold coin and will have equal number of apples and oranges.
Test 2: Chef will buy 1 orange by paying 1 gold coin and will have 5 apples and 3 oranges.

Codechef link: https://www.codechef.com/problems/FRUITS
'''

TestCases = int(input())
for i in range(TestCases):
 apples , oranges , coins = map(int, input().split())
 print(max(abs(apples -oranges)-coins,0))
