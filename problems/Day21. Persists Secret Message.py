'''
The Input conststs of two space.separated integers num' and nurn2. representing t e
message sent to the agency's computer (P) and the message sent to the technical head of the
agency (Q). respect tvely
Output
Pnnt an Integer representing the minimum number of bits that must be flipped to convert
o message Q

'''
n,k = input().split()
m1 = '{:0>8}'.format(str(bin(int(n)))[2:])
m2= '{:0>8}'.format(str(bin(int(k)))[2:])
count=0
for i in range(8):
    if m1[i]!=m2[i]:
        count+=1
print(count)
