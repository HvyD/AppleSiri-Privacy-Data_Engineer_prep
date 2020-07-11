"""
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Figure A), write a program to output the skyline formed by these buildings collectively (Figure B).

Buildings Skyline Contour
The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi], where Li and Ri are the x coordinates of the left and right edge of the ith building, respectively, and Hi is its height. It is guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0. You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .

The output is a list of "key points" (red dots in Figure B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. A key point is the left endpoint of a horizontal line segment. Note that the last key point, where the rightmost building ends, is merely used to mark the termination of the skyline, and always has zero height. Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as:[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].
"""

import heapq

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        rv = []
        # Sort by x coordinates asc and then size desc
        buildings.sort(key=lambda x:(x[0], -x[1], -x[2]))
        # Filter out small ones that don't affect skyline
        filtered = []
        for v in buildings:
            if not filtered:
                filtered.append(v)
                continue
            if v[1] > filtered[-1][1] or v[2] > filtered[-1][2]:
                filtered.append(v)
        points = sorted(list({(L, -H, R) if left else (R, 0, 0)
                              for L, R, H in filtered for left in [True, False]}))
        heap = [(0, float('inf'))]
        for x, negH, R in points:
            while x >= heap[0][1]:
                heapq.heappop(heap)
            if negH:
                heapq.heappush(heap, (negH, R))
            if not rv or rv[-1][1] + heap[0][0]:
                rv.append([x, -heap[0][0]])
        return rv
