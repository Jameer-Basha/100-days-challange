'''
Consider a rub-empty array ot inarrwith ttk' separated by and an nteger innum Find a runt*roumum boed on
below
• Identity au possibk: unque comtmations ot tour trom marr
e A uruqtr irrespective ot try: the same set appear n my other common
• l! there are one or more continat»onswtose sum or ekYtents equal to innum, set outturn wth the coug ot combinauns
• It there is no wnose sum to innum. pnnt -1
Assumption:
• at beast 4 elements
Input tormae
first One contains the array inarr wtth the eberrents separated by •.'(comma)
Second une contans the integer innum
Read the input from the standard input stream
Output tormae
pnnt outnum to the standard output stream

Sample Input 0

-1,1,0,0,2,-2
0
Sample Output 0

3
Explanation 0

We have three such quads: - -1,1,0,0 - 0,0,2,-2 - -1,1,2,-2

Hence, answer is 3.

Sample Input 1

8,4,3,0,2,5
8
Sample Output 1

-1
Explanation 1

No such combination possible, hence -1

'''

class Pair:
    def __init__(self, x, y):
        self.index1 = x
        self.index2 = y

def SummationSet(nums, target):
    map = {}
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            sum = nums[i] + nums[j]
            if sum not in map:
                map[sum] = [Pair(i, j)]
            else:
                map[sum].append(Pair(i, j))
    ans = set()
 
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            lookUp = target - (nums[i] + nums[j])
            if lookUp in map:
                temp = map[lookUp]
 
                for pair in temp:
                    if pair.index1 != i and pair.index1 != j and pair.index2 != i and pair.index2 != j:
                        l1 = [nums[pair.index1], nums[pair.index2], nums[i], nums[j]]
                        l1.sort()
                        ans.add(tuple(l1))
    return len(ans)
 
ls=list(map(int,input().split(",")))
n=int(input())
length=SummationSet(ls,n)
if(length!=0):
    print(length)
else:
    print(-1)
