"""
We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words.

You may return the list in any order.



Example 1:
Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]

Example 2:
Input: A = "apple apple", B = "banana"
Output: ["banana"]
"""


from collections import Counter

class Solution:
    def uncommonFromSentences(self, A, B):
        counter = Counter(c for c in (A + " " + B).split())

        return [k for k,v in counter.items() if v == 1]

obj = Solution()
assert(obj.uncommonFromSentences("this apple is sweet", "this apple is sour") == ["sweet", "sour"])
assert(obj.uncommonFromSentences( "apple apple", "banana") == ["banana"])
