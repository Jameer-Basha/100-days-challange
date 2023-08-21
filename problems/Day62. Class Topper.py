'''
Remove all duplicates for highest and second highest marks in a class and output the count of the deleted students.

Input Format

An array with marks of students.

Constraints

-

Output Format

A number representing students to be deleted.

Sample Input 0

1 2 3 4 3 1
Sample Output 0

1
Explanation 0

Highest marks are 4, second highest 3. At 3 marks we have two students. So one of them will be deleted. Hence, number of students to be deleted is 1.

'''

lst =list(map(int,input().split()))
set_lst=list(set(lst))
set_lst.sort()
Max1=set_lst[-1]
Max2=set_lst[-2]
Max1_count=0
Max2_count=0
for i in lst:
    if i== Max1:
        Max1_count+=1
    if(i== Max2):
        Max2_count+=1
    
print(Max2_count+Max1_count-2)
