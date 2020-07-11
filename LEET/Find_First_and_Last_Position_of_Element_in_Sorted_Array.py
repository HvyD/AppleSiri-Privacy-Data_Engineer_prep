

"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]



NON-BINARY-Search using Bisect
 Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        l = bisect.bisect_left(nums, target)
        r = bisect.bisect_right(nums, target)
        if l == r:
            return [-1, -1]
        return [l, r-1]
"""

class Solution:
    def searchRange(self, nums, target):
        def FirstOccurence(A,x):
            (left, right) = (0, len(A) - 1)
            result = -1

            while left <= right:
                mid = (left + right) // 2
                if x == A[mid]:
                    result = mid
                    right = mid - 1

                elif x < A[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            return result

        def LastOccurence(A, x):
            (left, right) = (0, len(A) - 1)
            result = -1

            while left <= right:
                mid = (left + right) // 2
                if x == A[mid]:
                    result = mid
                    left = mid + 1

                elif x < A[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            return result

        return (FirstOccurence(nums,target),LastOccurence(nums,target))


obj = Solution()
assert(obj.searchRange([5,7,7,8,8,10], 8) == [3,4])
