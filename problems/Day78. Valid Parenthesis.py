'''

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

'''


def isValid(string):
  push_lst = ["(","[","{"]
  pop_lst = [")","]","}"]
  
  brackets = ""
  for i in string:
   if i in push_lst:
    brackets+= i
   for j in range(3):
    if pop_lst[j]==i:
     if len(brackets)>0 and brackets[-1]==push_lst[j]:
      brackets = brackets[:len(brackets)-1]
     else:
      return False
   
  if len(brackets)!=0:
   return False
  
  return True
  
 
print(isValid("(()"))
