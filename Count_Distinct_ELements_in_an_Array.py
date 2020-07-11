
1. First  ask for basic simple solution
# O(NLogN)

from collections import Counter

def countDistinct(arr):
    return len(Counter(arr).keys())

arr = [10, 20, 20, 10, 20]

print(countDistinct(arr))  # => 2

2. Then ask for solution with better efficiency
# O(N) - using hashing more efficiently
def countDistinct(arr):
    n = len(arr)
    s = set()
    res = 0
    for i in range(n):
        if (arr[i] not in s):
            s.add(arr[i])
            res += 1
    return res

arr = [6, 10, 5, 4, 9, 120, 4, 6, 10]

print(countDistinct(arr))  # => 6


3. Then ask how this can be done on a Big Scale

1.arr = [1,4,3,2,5,2,1,3,2,1,4,2,1] => 5
# shuffle/Split
2a. [1,1,1,1] => 1
2b. [2,2,2,2] => 1
2c.[3,3,4,4,5] => 3
3. a+b+c => 5
