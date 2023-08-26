'''
Given N (Number of pizzas), M minimum number of people that must be there in the party, find P, number of people actually called so that all people get equal number of pizzas and no pizzas are left.

HINT IS THAT YOU MAY BE GIVEN LARGE PRIME NUMBERS AND IF YOU TRY TO GO TO N, IT WILL GIVE TIMEOUT. SO GO UP TO SQRT(N) only and if it has no factors then it is prime and ans would be N iteself.

Input Format

N M

Constraints

N up to 10^10

Output Format

-

Sample Input 0

18 4
Sample Output 0

6
Explanation 0

Greater than or equal to 4, smallest factor of 18 is 6. So 6 people can come to party and each one gets 3

'''


n,k=map(int,input().split())
while(n%k!=0):
    k+=1
print(k)
