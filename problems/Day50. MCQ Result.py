'''

You are given a function,
Int XQResu1t (int n, int key[), Int paper[l);
The function accepts two integer arrays key' ard 'paper' of len;th •n'
as its argu•nent. 'key' contains the correct answers of examination
ard •paper' contains be answers that a student has given, like {1, 2,
1, 3). Unanswered questions are denoted by -1. While xoring the
examination, a correct answer gets +3 marks, an ixorrect ænswer
gets -1 marks and an unanswered question gets O marks. Impiement
the function to calculate ard retum the result of a MCQ examination
by companng given 'paper' and key' sequentiatty.
Note:
Result lies within range.
Indexing starts
Assumption: n > 0
Example:
Input:
key: 3 2 4
paper: 223 3
3
Explanation:
and 3rd cueøons are correct and scores +3 marks. Yd, ace
questions are ard scores •1 marks. Thus, o..tput - (2 •

Sample Input
paper: 4 2 2 2

Sample Output
8

'''

key = list(map(int,input().split()))
paper = list(map(int,input().split()))
correct=0
incorrect=0
for i in range(len(key)):
    if(key[i]==paper[i]):
        correct+=1
    else:
        incorrect+=1
print(correct*3-incorrect)
