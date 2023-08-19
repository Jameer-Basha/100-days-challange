'''

Given  two robos robotop and robocop intial postions and 
robotop starts at Xth position and takes exactly T seconds to complete one lap
and robocop  starts at Yth position and takes exactly R seconds to complete one lap
you need to find time where robotop and robocop meet each other

Example:

input:
6
3
7
4

output: 15

in above exanple robotop starts at 6 and moves to 9,12,15,18,......
robocop starts at 7 and move to 11,15,19,23,....
so answer is 15

'''

def roborace(input1,input2,input3,input4):
    robotop= input1+input2
    robocop= input3+input4
    robotop_lst=[robotop]
    robocop_lst=[robocop]
    ans=0
    for i in range(1000):
        robotop+=input2
        robotop_lst.append(robotop)
    for i in range(1000):
        robocop+=input4
        robocop_lst.append(robocop)
    for i in robotop_lst:
        if i in robocop_lst:
            ans=i
            break
    return ans 

input1=int(input())
input2=int(input())
input3=int(input())
input4=int(input())
print(roborace(input1,input2,input3,input4))


