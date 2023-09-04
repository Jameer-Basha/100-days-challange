'''

You are given around five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list in sample is sorted into alphabetical order, PAMELA, which is worth , is the  name in the list. So, PAMELA would obtain a score of .

You are given  queries, each query is a name, you have to print the score.

Input Format

The first line contains an integer , i.e., number of names.
Next  lines will contain a Name.
Followed by integer  followed by  lines each having a word.

Constraints

length of each word will be less than 
Output Format

Print the values corresponding to each test case.

Sample Input

5
ALEX
LUIS
JAMES
BRIAN
PAMELA
1
PAMELA
Sample Output

240

'''

n=int(input())
lst=[]
for i in range(n):
    lst.append(input())
lst.sort()
q=int(input())
for i in range(q):
    name = input()
    upp= name.upper()
    Sum=0
    for i in upp:
        value = ord(i)-64
        Sum+=value
    print(Sum*(lst.index(name)+1))
