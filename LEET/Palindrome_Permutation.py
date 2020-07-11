"""
Given a string, determine if a permutation of the string could form a palindrome.

Example 1:

Input: "code"
Output: false
Example 2:

Input: "aab"
Output: true
Example 3:

Input: "carerac"
Output: true

"""
import collections

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        s=collections.Counter(s)
        ctr=0
        for idx,ele in s.items():
            if s.get(idx)%2:
                ctr+=1

            if ctr==2:
                return False


        return True

obj = Solution()
assert(obj.canPermutePalindrome("code") == False)
assert(obj.canPermutePalindrome("aab") == True)
assert(obj.canPermutePalindrome("carerac") == True)
