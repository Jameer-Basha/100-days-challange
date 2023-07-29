'''
EasyWay is an online exam for new graduates
of any disdpline to find enoy level Jobs in their
fields. The website generates the roll number
of its registered students with the help of the
students' application numbers. The process
includes a key K for generating an individual
roll number. To generate the roll number, each
digit in the application number is replaced by
the Kth digit that comes after it in the
application number. The series of digits is—
considered in a cyclic fashion for the last K

Write an algorithm to generate the roll number from the given application number.

Input Format

The input consists of two space-seperated positive integers- applicaNum and key, representing the application number and key(K), respectively.

Constraints

0 <* applicaNum* <- 10^9

Output Format

Print an integer representing the roll number.

Sample Input 0

43251 3
Sample Output 0

25143
Explanation 0

Replace 4 with 2;
        3 with 5;
        2 with 1;
        5 with 4;
        1 with 3.
       So the output is 25143

'''
n,k = map(int,input().split())
lst = list(str(n))
lst = lst[k-1:]+lst[:k-1]
res = "".join(str(i) for i in lst)
print(res)
