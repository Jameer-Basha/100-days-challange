'''

Alice is rearranging her library. She takes the innermost Shell and
reverses the order of books. She breaks the walls of the shelf. in
the end, there will be only books and no shelf walls.

Print the order of books.
Opening and closing walls of shelves are shown by '/' and '\'
respectively whereas books are represented by lower case
alphabets.

Input format

The first line contains string s displaying her library.

Output format

print only one string displayng Alice's library after rearrangement.

Sample Input:
/u/love\i\

Sample Output
iloveu

Explanation
/u/love\i\
Here Katrina breaks the inner most shelf and reverse the order So
the library will be /uevoli\. Now she breaks the outermost wall and reversde the order. so the library will be ilovey
'''

inp_data = [each for each in input()]

while inp_data[0]=='/':

    temp=[]

    i=0

    n=0

    search=chr(92)

    while inp_data[i]!=search:

        temp.append(inp_data[i])

        if inp_data[i]=='/':

            n=i

        i=i+1

    inp_data=inp_data[:n]+inp_data[i-1:n:-1]+inp_data[i+1:]

print(''.join(inp_data))
