def fib(x: int) -> int:
    n0 = 0
    n1 = 1
    for i in range(x):
        n0, n1 = n1, n1 + n0
    return n1

class Solution:
    def climbStairs(self, n: int) -> int:
        return fib(n)
