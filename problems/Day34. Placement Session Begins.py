''' 
The placement season has begun in a college. There are N number of students standing outside an interview room in a line. It is given that a person who goes in first has higher chances of getting selected.

Each student has a number associated with them known as the problem-sloving capability(PSC). The higher the capability the higher the chances of selection. Now, each student wants to know the number of students ahead of him/her who have more problem-sloving capability than him/her.

Find this number for each student.

Input Format

input1: An integer N, which denotes the number of students present.

input2: An array of size N, denoting the problem-sloving capability of the students.

Constraints

_

Output Format

An array of size N denoting the required answer for each student.

Sample Input 0

5 7 9 4 11 16 8
Sample Output 0

0 0 0 3 0 0 3
Explanation 0

There are 0 persons before first one, 0 before second who have more than 7, but 3 people before one who has a value 4 and so on.

'''
lst = list(map(int,input().split()))
res=[]
res.append(0)
for i in range(1,len(lst)):
    count=0
    for j in range(0,i):
        if(lst[i]<lst[j]):
            count+=1
    res.append(count)
ans=" ".join(str(i) for i in res)
print(ans)
