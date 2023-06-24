''' 
Question 2: Sorting of numbers

Given two arrays marks and names. You have to arrange the names array in sorted order without disturbing the linking of marks and names.
Return marks array after the sorting.

Example 1:
Input: marks = [10, 20, 30, 50], names = ["Joe", "Raj", "Hari", "John"]
Output: [30, 10, 50, 20]
Explanation: arrange the names in sorted order.
Thus names will be ["Hari", "Joe","John","Raj"]
Thus marks will be [30, 10, 50, 20]

Note: Dictionary should not be used
''' 
names =list(input("Enter the names of the student" ).split())
marks= list(map(int,input("Enter marks of Students in one line seperated by space  ").split()))
names_copy=names.copy()
names_copy.sort()
res=[]
print(names_copy)
for i in names_copy:
	ind= names.index(i)
	res.append(marks[ind])
print(res)
