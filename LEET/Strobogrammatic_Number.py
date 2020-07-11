"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

Example 1:
Input:  "69"
Output: true

Example 2:
Input:  "88"
Output: true

Example 3:
Input:  "962"
Output: false

"""

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        d = {1:1,6:9,8:8,9:6,0:0}
        new_num = ''
        for l in num:
            if int(l) in d:
                new_num += str(d[int(l)])
        if new_num[::-1] == num:
            return True
        return False


obj = Solution()
assert(obj.isStrobogrammatic("69") == True)
assert(obj.isStrobogrammatic("88") == True)
assert(obj.isStrobogrammatic("962") == False)
