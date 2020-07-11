
#N-Repeated Element in Size 2N Array

"""
In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.
Return the element repeated N times.

Example 1:
Input: [1,2,3,3]
Output: 3

Example 2:
Input: [2,1,2,5,3,2]
Output: 2

Example 3:
Input: [5,1,5,2,5,3,5,4]
Output: 5
"""

from collections import Counter

class Solution(object):
    def repeatedNTimes(self, A):
        count = Counter(A)
        for k in count:
            if count[k] > 1:
                return k

obj = Solution()
assert(obj.repeatedNTimes([1,2,3,3]) == 3)
assert(obj.repeatedNTimes([5,1,5,2,5,3,5,4]) == 5)
assert(obj.repeatedNTimes([2,1,2,5,3,2]) == 2)
