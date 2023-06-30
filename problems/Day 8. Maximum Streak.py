'''
Question  :Maximum Streak

CodeChef offers a feature called streak count. A streak is maintained if you solve at least one problem daily.

Om and Addy actively maintain their streaks on CodeChef. Over a span of N consecutive days, you have observed the count of problems solved by each of them.

Your task is to determine the maximum streak achieved by Om and Addy and find who had the longer maximum streak.

Input Format

The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of multiple lines of input.
The first line of each test case contains an integer N  the number of days.
The second line of each test case contains N space-separated integers, the representing the problems solved by Om on each
The third line of each test case contains N space-separated integers,  representing the problems solved by Addy on each day

Output Format

For each test case, output:

OM, if Om has longer maximum streak than Addy;
ADDY, if Addy has longer maximum streak than Om;
DRAW, if both have equal maximum streak.

You may print each character in uppercase or lowercase. For example, OM, om, Om, and oM, are all considered the same.

Constraints
1≤T≤10 
1≤N≤10
The sum of N over all test cases won't exceed 6 * 10 ^5 

Input : 

Test cases : 3

Test case 1 
No of days 6
Om solved problems 1 7 3 0 2 13
Adday solved problems 0 2 3 4 5 0

Test case2 
No of days 3
Om solved problems 1 3 4
Adday solved problems 3 1 2

Test case 3
No of days 5
Om solved problems 1 2 3 0 1
Adday solved problems 1 2 0 2 3
 
Output :

Test case 1 Addy
Test case 2 Draw
Test case 3 Om


Code chef link : https://www.codechef.com/problems/CS2023_STK
'''



 MaxStreak( Om_arr , Addy_arr):
 MaxStreak_Om =0
 MaxStreak_Addy=0
 OmStreak= 0
 AddyStreak= 0
 Streak =0
 for i in Om_arr:
  if i == 0:
   Streak = 0
  else:
   Streak +=1 
  MaxStreak_Om = max(MaxStreak_Om , Streak)
 Streak = 0
 for i in Addy_arr:
  if i == 0:
   Streak = 0
  else:
   Streak +=1 
  MaxStreak_Addy = max(MaxStreak_Addy , Streak)
 if (MaxStreak_Om == MaxStreak_Addy):
  print('Draw')
 elif(MaxStreak_Om > MaxStreak_Addy):
  print('Om')
 else:
  print('Addy')
  
TestCases = int(input())
for i in range(TestCases):
 days = int(input())
 Om_arr = list(map(int , input().split()))
 Addy_arr = list(map(int,input().split()))
 MaxStreak(Om_arr , Addy_arr)
