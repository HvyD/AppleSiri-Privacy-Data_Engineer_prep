"""
We define a harmounious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

Example 1:

Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].

 """

from collections import Counter

class Solution:
    def findLHS(self, nums):
        d=Counter(nums)
        max_count=0
        for num in d:
            if num+1 in d:
                max_count=max(max_count, d[num]+d[num+1])
        return max_count

obj = Solution()
assert(obj.findLHS([1,3,2,2,5,2,3,7]) == 5)
