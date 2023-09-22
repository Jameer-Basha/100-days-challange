'''

Last Digit Array
you are provided an array of size N that contains non Negative integers.
Your task is to determine whether that number is formed by selecting the last digit of all tho N numbers are divisible by 10.
Note: View the sample explanation section for more clarificatton.
Input Format:
• First line: A Single integer N denoung the Site of array A
• N integers follow that are part of tho array

Output Format:
If the number is divisible by 10, then print Yes. Otherwise, print NO


Sample Input:
5
85
25
65
21
84

Sample Output:
No

Explanation
Last digit of 85 is 5.
Last digit of 25 is 5.
Last digit of 65 is 5.
Last digit of 21 is 1.
Last digit of 84 is 4.
Therefore the number formed IS 55514 which IS not divisible by 10.
'''

t=int(input())
s=""
for i in range(t):
  n=int(input())
  s+=str(n%10)

if(int(s)%10==0):
  print("YES")
else:
  print("NO")
