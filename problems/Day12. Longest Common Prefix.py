'''

✅ Question 12: Longest Common Prefix


Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

📌Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.

🔗 Link: https://leetcode.com/problems/longest-common-prefix/description/

'''

def longestCommonPrefix(arr):
 Result = ""
 arr.sort()
 first = arr[0]
 last =arr[-1]
 small = min(len(first), len(last))
 for i in range(small):
  if(first[i] != last[i]):
   break
  Result += first[i]
 return Result 

lst= list(input().split())
print(longestCommonPrefix(lst))
