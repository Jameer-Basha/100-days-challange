'''
Sasuke being one ot the most powerful Ninjas in the world. is being faced with 'N' number 01
shinobis. Each shinobi •i' (O i < N) has 'Ci• (1 100000) chakras. With a single
shot or a lightening blade or strength Sasuke can reduce the chakra level ot each
shinobi 'i' to a maximum of (CI-k, O).
Sasuke now wants to reduce the sum or chakra levet of atl shinobi to utmost
You need to help Sasuke return the minimum strength ot a lightning blade attack that can
achieve this task.
Input Format
Input Specification:
Inputl: An Integer value N representing the number ot shinobs where (1
N 1000).
Input2: An Integer array, containing the chakra Seveis ot N shir•obis
Input3: An Inteaer value S, the maximum sum ot chakra levels after the attack

'''
n = int(input())
l = list(map(int,input().split()))
c = int(input())
max = 0 
for i in range(0,n):
    if max<l[i]-c :
        max = l[i]-c
print(max)
