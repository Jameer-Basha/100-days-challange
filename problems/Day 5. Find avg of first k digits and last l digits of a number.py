''' 
Question :Find the average of k digits from the beginning and l digits from the end of the given number

Given three integers N, K and L. The task is to find the average of the first K digits and the last L digits of the given number N without any digit overlapping.

Example 1:
Input: N = 123456, K = 2, L = 3 
Output: 3.0 
Sum of first K digits will be 1 + 2 = 3 
Sum of last L digits will be 4 + 5 + 6 = 15 
Average = (3 + 15) / (2 + 3) = 18 / 5 = 3

Example 2 :
Input: N = 456966, K = 1, L = 1 
Output: 5.0
'''

def average(n , k, l):
	n=str(n)
	sum_first_k =0
	sum_last_l =0
	lst = list(map(int , n))
	length = len(lst)
	for i in range(k):
		sum_first_k += lst[i]
	for i in range(l):
		sum_last_l +=lst[length-i-1]
	avg = (sum_first_k + sum_last_l) /(k+l)
	return avg 

n= int(input("Enter the Number"))
k=int(input("Enter k value "))
l=int(input("Enter l value"))
print(average(n,k,l))
