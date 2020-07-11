"""
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:
Input: "3+2*2"
Output: 7

Example 2:
Input: " 3/2 "
Output: 1

Example 3:
Input: " 3+5 / 2 "
Output: 5
"""
import operator

class Solution:
    def calculate(self, s: str) -> int:
        return self.calc(s, 0)[0]

    def calc(self, s, i):
        pre, cur, ans, sign = 0, 0, 0, "+"
        while i < len(s):
            c = s[i]
            if c.isdigit():
                cur = cur * 10 + int(c)
            if c in "+-*/" or i == len(s) - 1 or c == ')':
                if sign == "+":
                    ans += pre
                    pre = cur
                elif sign == "-":
                    ans += pre
                    pre = -cur
                elif sign == "*":
                    pre *= cur
                elif sign == '/':
                    pre = int(operator.truediv(pre, cur))
                cur = 0
                sign = c
            elif c == '(':
                ret , i =  self.calc(s, i + 1)
                ans += -ret if sign == '-' else ret
            if c == ')':
                return ans + pre, i
            i += 1
        return ans + pre, i

obj = Solution()
assert(obj.calculate("3+2*2") == 7)
assert(obj.calculate(" 3/2 ") == 1)
assert(obj.calculate( "3+5/2") == 5)
