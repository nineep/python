class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        xor = 0
        for i in range(n):
            num = start + 2*i
            # print(num)
            if num == start:
                xor = num ^ xor
            else:
                xor = num ^ xor
        return xor
a = Solution().xorOperation(10, 5)
print(a)