'''

Question : Find Key

You are provided with 3 numbers input1, input2 and input3.
Each of these are four digit numbers within the range >= 1000 and <= 9999.
i.e , 
1000 <= input1 <= 9999
1000 <= input2 <= 9999
1000 <= input3 <= 9999

You are expected to find the Key using the below formula -
Key = (LARGEST digit in the thousands place of all three numbers - smallest digit in the thousands place of all three numbers] [LARGEST digit in the hundreds place of all three numbers - smallest digit in the hundreds place of all three numbers] [LARGEST digit in the tens place of all three numbers - smallest digit in the tens place of all three numbers] [LARGEST digit in the units place of all three numbers smallest digit in the units place of all three numbers]

Example:
input1 = 3521, input2=2452, input3= 1352,
then Key= [3-1] [5-3] [5-2] [2-1] = 2231

'''

def findMaxMin( n1, n2 ,n3):
 Max = int (max( n1 , n2 ,n3 ) )
 Min = int ( min ( n1 , n2 , n3 ))
 return Max-Min

def findKey(nums1 , nums2, nums3):
 thous = findMaxMin(nums1[0],nums2[0],nums3[0])
 hund = findMaxMin(nums1[1], nums2[1] , nums3[1])
 tens = findMaxMin(nums1[2], nums2[2] , nums3[2])
 units =findMaxMin(nums1[3], nums2[3] , nums3[3])
 result  = thous* 1000 + hund * 100 + tens * 10 + units
 return result 

input1 = input("Enter 1st input")
input2 = input("Enter 2nd input")
input3 = input("Enter 3rd input")

print(findKey(input1,input2,input3))

#Find Key 26 -06-2023
