"""
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.



Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true

"""

class Solution:
    def canConstruct(self, ransomNote, magazine):
        mag=list(magazine)
        for i in ransomNote:
            if i in mag:
                mag.remove(i)
            else:
                return False
        return True

obj = Solution()
assert(obj.canConstruct("a", "b") == False)
assert(obj.canConstruct("aa", "ab") == False)
assert(obj.canConstruct("aa","aab") == True)
