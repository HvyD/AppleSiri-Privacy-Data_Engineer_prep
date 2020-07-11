"""
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

"""

class Solution:
    def countPrimes(self, n):
        prime, nn = [True] * (n), 0
        for i in range(2, n):
            if prime[i]:
                j, nn = 2, nn + 1
                while j * i < n:
                    prime[j * i] = False
                    j += 1
        return nn

obj = Solution()
assert(obj.countPrimes(10) == 4)
