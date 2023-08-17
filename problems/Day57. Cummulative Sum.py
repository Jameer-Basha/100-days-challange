'''

Given an array [1,2,3,4,5]

You have to return an array which has elements as absolute difference between prefix and suffix sum

Abs(1-(2+3+4+5))=13 Abs((1+2)-(3+4+5))=9 Abs((1+2+3)-(4+5))=3 Abs((1+2+3+4)-(5))=5 Abs((1+2+3+4+5)-0)=15 The array to be returned is [13,9,3,5,15]

Input Format

Single line with given elements of the array.

Constraints

n<=10^5

Output Format

Print the values in output.

Sample Input 0

1 2 3 4 5
Sample Output 0

13 9 3 5 15

'''

lst = list(map(int,input().split()))
res=[]
for i in range(len(lst)):
    sub1=lst[:i+1]
    sub2 = lst[i+1:]
    Sum =abs(sum(sub1)-sum(sub2))
    res.append(Sum)
ans =" ".join(str(i) for i in res)
print(ans)
