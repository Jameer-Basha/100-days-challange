''' 
Question :Covid and Theatre Tickets

Mr. Chef is the manager of the Code cinemas and after a long break, the theatres are now open to the public again. To compensate for the loss in revenue due to Covid-19, Mr. Chef wants to maximize the profits for every show from now on and at the same time follow the guidelines set the by government. The guidelines are:

. If two people are seated in the same row, there must be at least one empty seat between them.

.If two people are seated in different rows, there must be at least one completely empty row between them. That is, if there are people seated in rows i and j where i<j, there must be some row k such that i<k<j and nobody is seated in row k.
Given the information about the number of rows and the number of seats in each row, find the maximum number of tickets Mr. Chef can sell.

Input Format

The first line of input will contain a single integer T, denoting the number of test cases. The description of T test cases follows.
Each test case consists of a single line of input containing two space-separated integers N, M — the number of rows and the number of seats in each row, respectively.

Output Format
For each test case, output a single line containing one integer – the maximum number of tickets Mr. Chef can sell.

Constraints
1≤T≤100
1≤N,M≤100

Example 1:

Input 
Test cases : 3
1 5
3 3
4 4

Output: 
3
4
4

Explanation:
Test Case 1: There is only one row with five seats. Mr. Chef can sell a maximum of 3 tickets for seat numbers 1, 3 and 5.

Test Case 2: There are three rows with three seats each. Mr. Chef can sell a maximum of 4 tickets, for seats at the start and end of row numbers 1 and 3.

Test Case 3: There are four rows with four seats each. Mr. Chef can sell a maximum of 4 tickets, for example by choosing the seats at the start and end of row numbers 1 and 4.


Codechef link : https://www.codechef.com/problems/COVID_19

'''  


# cook your dish here
def maxSeats(rows, cols):
    maxSeatPerCol = (cols+1)//2
    maxSeatPerRow = (rows+1)//2
    
    return maxSeatPerRow*maxSeatPerCol
    
T = int(input())

for _ in range(T):
    row, col = map(int, input().split())
    
    print(maxSeats(row, col))
