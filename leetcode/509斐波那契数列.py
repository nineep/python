class Solution:
    def fib(self, N: int) -> int:
        # 0, 1, 1, 2, 3, 5, 8, 13...
        if N <= 1:
            return N

        a, b = 0, 1
        # for n in range(N-1):
        #     a, b = b, a+b
        # return b
        while N > 1:
            a, b = b, a+b
            N -= 1
        return b


r = Solution().fib(6)
print(r)
