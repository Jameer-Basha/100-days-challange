'''
Write a function which accepts three numbers and returns True if a) one of the three numbers is "close" to any one of the other numbers (differing from a number by at most 1), and b)Number that is left out is "far", differing from both other values by 2 or more. Return false if the above mentioned conditions are not satisfied

Sample Input Expected Output 4,1,3 True 5,6,7 False

Input Format
list of three numbers

Output Format
True or False

Sample Input 0
4,1,3

Sample Output 0
True

Sample Input 1
5,6,7

Sample Output 1
False

'''


x, y, z = map(int, input().split(','))

def chk(x, y, z):
    lst = sorted([abs(x-y), abs(y-z), abs(x-z)])
    
    if lst[0]<=1 and lst[1]>1 and lst[2]>1:
        return True
    return False

print(chk(x, y, z))
