"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:

Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""

from collections import deque

class Solution:
    def totalNQueens(self, n):
        placements = deque()
        for j in range(n):
            placements.append([j])

        for i in range(1, n):
            while placements and len(placements[0]) == i:
                aPlacement = placements.popleft()
                for j in range(n):
                    allowed = True
                    for itemI in range(len(aPlacement)):
                        if j == aPlacement[itemI] or j+i == aPlacement[itemI]+itemI or j-i == aPlacement[itemI]-itemI:
                            allowed = False
                            break
                    if allowed:
                        placements.append(aPlacement+[j])
        #print(placements)
        return len(placements)

obj = Solution()
assert(obj.totalNQueens(4) == 2)
