'''
Input is a string with several words. A word is considered hard:

1) If it has more consonants than vowels.

2) If it has three consecutive consonants.

Otherwise a word is easy. Input has only small case and spaces.

DIfficulty quotient = 5*(hard)-2*(easy)

Given a sentence compute its difficulty quotient.

Must use a function def difficultyQuotient(string):

If the string is Null, the function should return None, else the value of difficulty quotient.

Input Format

Sentence

Constraints

-

Output Format

Integer

Sample Input 0

qiewldoaa life ace by fantasy
Sample Output 0

11
Explanation 0

Hard words are:

qiewldoaa - it has three consequtive consnants wld

by

fantasy

Easy words are life ace.

So 3*5 - 2*2 = 11

'''
lst = list(input().split())
vowels=["a","e","i","o","u"]
harder_count =0
easy_count=0

for i in lst:
    vowel_count=0
    cons_count=0
    mode =0
    for j in range(len(i)):
        if i[j] in vowels:
            vowel_count+=1
        else:
            cons_count+=1
    for j in range(1,len(i)-1):
        if ((i[j-1] not in vowels) and (i[j] not in vowels) and (i[j+1] not in vowels)):
            mode=1
            harder_count+=1
            break
    #print(vowel_count , cons_count)
    if vowel_count>=cons_count and not mode:
        easy_count+=1
    elif cons_count>vowel_count:
        harder_count+=1
print(harder_count*5-2*easy_count)
