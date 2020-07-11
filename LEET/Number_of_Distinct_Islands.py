"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

Example 1:
11000
11000
00011
00011
Given the above grid map, return 1.

Example 2:
11011
10000
00001
11011
Given the above grid map, return 3.

Notice that:
11
1
and
 1
11
are considered different island shapes, because we do not consider reflection / rotation.

"""

class Solution:
    def numDistinctIslands(self, grid: List[List[str]]) -> int:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def dfs(r, startR,  c, startC):
            nonlocal coords
            coords += str(r-startR+1) + str(c-startC+1)
            grid[r][c] = 0
            for d in directions:
                r0 = r + d[0]
                c0 = c + d[1]
                if    r0 < len(grid) and c0 < len(grid[0]) \
                  and r0 >= 0        and c0 >= 0           \
                  and grid[r0][c0] == 1:
                    dfs(r0, startR, c0, startC)
        distinct = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    coords = ""
                    dfs(r, r, c, c)
                    distinct.add(coords)
        return len(distinct)
        
