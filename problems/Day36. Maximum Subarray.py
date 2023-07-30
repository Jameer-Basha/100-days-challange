'''
We define subsequence as any subset of an array. We define a subarray as a contiguous subsequence in an array.

Given an array, find the maximum possible sum among:

all nonempty subarrays.
all nonempty subsequences.
Print the two values as space-separated integers on one line.

Note that empty subarrays/subsequences should not be considered.

'''
def maxSubarray(arr):
    # Write your code here
    Max = max(arr)
    if(Max<0):
        return [Max,Max]
    subseq_sum=0
    subarr_sum=0
    sum_till=0
    for i in arr:
        if i>0:
            subseq_sum+=i
        sum_till+=i
        if(sum_till<0):
            sum_till=0
        if(sum_till>subarr_sum):
            subarr_sum=sum_till
    return(subarr_sum, subseq_sum)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
