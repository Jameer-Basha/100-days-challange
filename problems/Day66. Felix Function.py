
'''
F(0) = 1, F(1) = 1

F(N) = (F(N-1)+ 7*F(N-2) + N/4)modulo 1e9+7

HINT DO NOT USE RECURSION YOU WILL GET TIME OUT. USE LISTS to STORE values.

Input Format

N

Constraints

-

Output Format

Value of Felix Function

Sample Input 0

2
Sample Output 0

8
Explanation 0

F(2) = (F(1) + 7*F(0) + 2/4)%1000000007 This equals 8. 2//4 is 0 not .5


'''

def fellis(n):
    if n == 0 or n == 1:
        return 1
    
    modulo = 10**9 + 7
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] + 7 * dp[i - 2] + i // 4) % modulo
    
    return dp[n]

n=int(input())
print(fellis(n))
