'''

#User function Template for python3

class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr,n):
        ##Your code here
        #Return true or false
        Sum=0
        Set=set()
        for i in arr:
            Sum+=i
            if Sum in Set or Sum==0:
                return True
            else:
                Set.add(Sum)
        return False

'''


#User function Template for python3

class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr,n):
        ##Your code here
        #Return true or false
        Sum=0
        Set=set()
        for i in arr:
            Sum+=i
            if Sum in Set or Sum==0:
                return True
            else:
                Set.add(Sum)
        return False
