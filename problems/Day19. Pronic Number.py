'''
A pronic number is a number which is the product of two consecutive integers, that is, a number of the form n(n + 1). The first few pronic numbers are: 2, 6, 12, 20, 30,etc.

Ex: 6->2*3 it’s a pronic

12->3*4 it’s a pronic

Given an integer, identify all pronic numbers present in that integer and output them in sorted order.

For example

Input1: 93012630

In this the pronic numbers are Output2: 2 6 12 30 930

For all the substrings in the string, we should identify all the pronic numbers and output the pronic numbers present in sorted order. If no pronic number is present output -1.

Input Format

Read a number

Constraints

Number <=10^18

Output Format

print all the pronic numbers present in the string in sorted order.

Sample Input 0

93012630
Sample Output 0

2,6,12,30,930
Sample Input 1

4567
Sample Output 1

6,56

'''

def is_pronic(num):

    # Check if a number is a pronic number (n*(n+1))

    root = int(num ** 0.5)

    return root * (root + 1) == num and num != 0

def find_pronic_numbers(input_str):

    pronic_numbers = set()  # Use a set to store pronic numbers and avoid duplicates

    n = len(input_str)

    for i in range(n):

        for j in range(i + 1, n + 1):

            substr = int(input_str[i:j])

            if is_pronic(substr):

                pronic_numbers.add(substr)

    if pronic_numbers:

        pronic_numbers = sorted(pronic_numbers)  # Sort the pronic numbers before returning

        return pronic_numbers

    else:

        return -1

# Main function to read input and display output

if __name__ == "__main__":

    input_num = input().strip()

    result = find_pronic_numbers(input_num)

    

    if result == -1:

        print(-1)

    else:

        print(','.join(map(str, result)))
