"""
Given N axis-aligned rectangles where N > 0, determine if they all together form an exact cover of a rectangular region.

Each rectangle is represented as a bottom-left point and a top-right point. For example, a unit square is represented as [1,1,2,2]. (coordinate of bottom-left point is (1, 1) and top-right point is (2, 2)).


Example 1:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [3,2,4,4],
  [1,3,2,4],
  [2,3,3,4]
]

Return true. All 5 rectangles together form an exact cover of a rectangular region.




Example 2:

rectangles = [
  [1,1,2,3],
  [1,3,2,4],
  [3,1,4,2],
  [3,2,4,4]
]

Return false. Because there is a gap between the two rectangular regions.




Example 3:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [3,2,4,4]
]

Return false. Because there is a gap in the top center.




Example 4:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [2,2,4,4]
]

Return false. Because two of the rectangles overlap with each other.

"""
import collections

class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        ma, mb, mc, md = float('inf'), float('inf'), float('-inf'), float('-inf')
        count = collections.defaultdict(int)
        expected = calculated = 0
        for a,b,c,d in rectangles:
            ma = min(ma, a)
            mb = min(mb, b)
            mc = max(mc, c)
            md = max(md, d)
            count[(a,b)] += 1
            count[(c,d)] += 1
            count[(a,d)] += 1
            count[(c,b)] += 1
            expected += (c-a)*(d-b)
        calculated = (mc-ma)*(md-mb)

        allow = {(ma,mb), (ma,md), (mc,md), (mc,mb)}
        for point in count:
            if count[point]!=2 and count[point]!=4:
                if point not in allow:
                    return False
        return expected == calculated and len(set([tuple(n) for n in rectangles])) == len(rectangles)

obj = Solution()
assert(obj.isRectangleCover([
  [1,1,3,3],
  [3,1,4,2],
  [3,2,4,4],
  [1,3,2,4],
  [2,3,3,4]
]) == True)


assert(obj.isRectangleCover([
  [1,1,2,3],
  [1,3,2,4],
  [3,1,4,2],
  [3,2,4,4]
]) == False)
