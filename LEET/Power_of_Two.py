"""
Given an integer, write a function to determine if it is a power of two.

Example 1:
Input: 1
Output: true
Explanation: 20 = 1

Example 2:
Input: 16
Output: true
Explanation: 24 = 16

Example 3:
Input: 218
Output: false

"""

class Solution:
    def isPowerOfTwo(self, n):
        while n > 0:
            if n == 1:
                return 1
            if n % 2 != 0:
                return 0
            n = n / 2

obj = Solution()
assert(obj.isPowerOfTwo(1) == True)
assert(obj.isPowerOfTwo(16) == True)
assert(obj.isPowerOfTwo(218) == False)
