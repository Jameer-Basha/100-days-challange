''' 
Question :Stock and Prices

Chef wants to buy a stock whose price was S rupees when the market opened. He will buy the stock if and only if its price is in the range [A, B] The price of the stock has changed by C% by the time he was trying to buy the stock. Will he be able to buy the stock?

Input Format

First line of the input contains T, the number of testcases. Then the test cases follow.

Each test case contains 4 space-separated integers S, A,B,C in a single line.

Output Format

For each test case, if Chef buys the stock print YES, otherwise print NO.

You may print each character of the string in uppercase or lowercase (for example, the strings yEs, yes, Yes, and YES will all be treated as identical).

Constraints

1≤T≤1000

0≤S≤10 ^ 6

0≤A≤B≤10^6

-100≤C≤100


Example 1 : 

Input : 
Test cases :3
Test case 1: 100 93 108 7
Test case 2: 100 94 100 -7
Test case 3: 183 152 172 -17

Output :

Yes
No
No

Explanation:

Test Case 1: The price of the stock after gaining 7% will become 107, which is in Chef's range of [93, 108] Hence, Chef will buy the stock.

Test Case 2: The price of the stock after falling 7% will become 93, which is not in Chef's range of [94, 100] Hence, Chef will not buy the stock.
Test Case 3: The price of the stock after falling %17% will become 151.89, which is not in Chef's range of [152, 172] Hence, Chef will not buy the stock.

Codechef link : https://www.codechef.com/problems/CSTOCK

'''  


def finalValue(base, perc): 
    return base+(base*perc/100) 
def isInRange(left, right, val): 
    if (left<=val) and (right>=val): 
        return "YES" 
    else: 
        return "NO" 
     
T = int(input()) 
for i in range(T): 
    lst = list(map(int, input().split())) 
    value = finalValue(lst[0], lst[3]) 
    print(isInRange(lst[1], lst[2], value))
