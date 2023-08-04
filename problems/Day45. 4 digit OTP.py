'''

You will be given a number in the form of string, extract out digits at odd places, square & merge them. First 4 digits will be the required OTP.

Input :

First Input : String

Output : 4 digit OTP

Input Format

Read a Number in the form of String

Output Format

display 4 Digit OTP

Sample Input 0

34567
Sample Output 0

1636
Sample Input 1

11111111
Sample Output 1

1111

'''

s=input()
otp=""
for i in range(len(s)):
    if(i%2 !=0):
        otp+=str(int(s[i])**2)
print(otp[:4])
