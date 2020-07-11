"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
The same repeated number may be chosen from candidates unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[[7], [2,2,3]]


Example 2:
Input: candidates = [2,3,5], target = 8,
A solution set is:
[[2,2,2,2], [2,3,3], [3,5]]

"""

class Solution:
    def combinationSum(self, candidates, target):
        if target < min(candidates):
            return []

        dp = [[[]]] + [[] for _ in range(target)]

        for can in candidates:
            for j in range(can,target+1):
                for lst in dp[j-can]:
                    dp[j].append(lst + [can])

        return dp[-1]

obj = Solution()
assert(obj.combinationSum([2,3,6,7], 7) == [[2, 2, 3], [7]])
assert(obj.combinationSum([2,3,5], 8) == [[2,2,2,2], [2,3,3], [3,5]])
