'''

Write a program to input an array of elements from the user and return the possible largest value using the elements.


For example, 
if the given numbers are {54, 546, 548, 60}, the arrangement 6054854654 gives the largest value. And if the given numbers are {1, 34, 3, 98, 9, 76, 45, 4}, then the arrangement 998764543431 gives the largest value.



Sample Input and Output:
Input:
4 ->Sizeof an array

54

546

548

60

Output:
6054854654

'''
from itertools import permutations
 #permutations of the list values
def biggest_number(l):
    list = []
    for a in permutations(l, len(l)):
        
        list.append("".join(map(str,a)))  
    return max(list)

arr = list(map(int, input('Enter the elements of a list: ').split()))
print(biggest_number(arr)) 
