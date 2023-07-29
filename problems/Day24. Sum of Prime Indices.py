'''
Given an array as input, return the sum of all elements that are at prime indices. Prime indices are 2, 3, 5, and so on. The index is 0 based.

Input Format
Elements of the array

Constraints

elements < 10^5

Output Format

sum of all the elements at prime indices

Sample Input 0

5 9 6 2 4 3 4 8 9
Sample Output 0

19
Explanation 0

Numbers at 2,3,5,7 indices are 6 2 3 8 and their sum is 19

'''
lst =list(map(int,input().split()))

def isPrimeIndex(n):
    root = n**(0.5)
    if (n<2):
        return False
    for i in range(2,int(root)+1):
        if(n%i==0):
            return False
    return True

count=0
for i in range(len(lst)):
    if(isPrimeIndex(i)):
        count+=lst[i]
print(count)
