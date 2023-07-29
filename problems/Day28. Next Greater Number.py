'''
Given a number 'N'(containing at most 10,000 digits), find the next greater number having the same digits. it is guaranteed that there exists a next greater number having the same digits as N

Input Format

input1: the length of the string 'N' input2: the number 'N' in the form of a string.

Constraints

_

Output Format

return the next generator number having the same digits as 'N' in the form of a string.

Sample Input 0

6
534976
Sample Output 0

536479
Explanation 0

To Generate Next Greater Number:

For Example: - if the input number is “534976”, we stop at 4 because 4 is smaller than next digit 9. If we do not find such a digit, then output is “Not Possible”.

Now search the right side of above found digit ‘d’ for the smallest digit greater than ‘d’. For “534976″, the right side of 4 contains “976”. The smallest digit greater than 4 is 6.

Swap the above found two digits, we get 536974 in above example.

Now sort all digits from position next to ‘d’ to the end of number. The number that we get after sorting is the output. For above example, we sort digits in bold 536974. We get “536479” which is the next greater number for input 534976.

'''
def nextNum(number,n):
    
     for i in range(n-1,0,-1):
         if number[i] > number[i-1]:
             break
                
     x = number[i-1]
     smallest = i
     for j in range(i+1,n):
         if number[j] > x and number[j] < number[smallest]:
             smallest = j
           
     number[smallest],number[i-1] = number[i-1], number[smallest]
       
     x = 0
     for j in range(i):
         x = x * 10 + number[j]
       
     number = sorted(number[i:])
     for j in range(n-i):
         x = x * 10 + number[j]
       
     print (x)

n=int(input())
s=input()
number = list(map(int ,s))
nextNum(number, len(s))

