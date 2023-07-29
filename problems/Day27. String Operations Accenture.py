'''
Ralph is Learning about strings and his tutor gave him a task as homework. Tutor mailed the following question to Ralph.

Consider an integer p and two strings M and N. Find out whether we can convert M to N by performing exactly P of the given operations on

1) Insert a lowercase alphabetic letter to the end of M.

2) Remove the last character in M.

Ralph is anxious as he felt the question is hard and adding to that, this is his first task. He pinged his facebook friend and that is You!

Input Format

The first line will contain string M, second line will contain string N and the third line will contain a positive integer P.

Constraints

Performing the Delete operation on an empty string will result in an empty string.

Output Format

if M is converted to N by performing the operations specified, then print "True" else print "False".

Sample Input 0

pqruvs
pqrxy
5
Sample Output 0

True
Explanation 0

3 delete operations and 2 Insert operations to convert pqruvs to pqrxy
'''
def can_convert_strings(M, N, P):
    prefix= 0
    min_length = min(len(M), len(N))

    
    while prefix< min_length and M[prefix] == N[prefix]:
        prefix += 1

    
    remaining_ops = (len(M) - prefix) + (len(N) - prefix)

    
    return remaining_ops <= P


M = input().strip()
N = input().strip()
P = int(input().strip())


result = can_convert_strings(M, N, P)
print("True" if result else "False")
