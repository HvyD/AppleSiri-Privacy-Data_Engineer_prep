"""
Given a binary tree, you need to find the length of Longest Consecutive Path in Binary Tree.

Especially, this path can be either increasing or decreasing. For example, [1,2,3,4] and [4,3,2,1] are both considered valid, but the path [1,2,4,3] is not valid. On the other hand, the path can be in the child-Parent-child order, where not necessarily be parent-child order.

Example 1:

Input:
        1
       / \
      2   3
Output: 2
Explanation: The longest consecutive path is [1, 2] or [2, 1].


Example 2:

Input:
        2
       / \
      1   3
Output: 3
Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0, 0 # [des, inc] toward root, they are the lengths in the two directions along parent-child relation

            res = [1, 1]
            l = dfs(node.left)
            r = dfs(node.right)
            if node.left and abs(node.val - node.left.val) == 1:
                i = (node.val - node.left.val + 1) // 2
                res[i] = max(res[i], l[i] + 1)
            if node.right and abs(node.val - node.right.val) == 1:
                i = (node.val - node.right.val + 1) // 2
                res[i] = max(res[i], r[i] + 1)

            self.res = max(self.res, sum(res)-1)
            return res

        self.res = 0
        dfs(root)
        return self.res
