class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum = 0
        product = 1
        for num in str(n):
            product = product * int(num)
            sum += int(num)
        return product - sum

a = Solution().subtractProductAndSum(4421)
print(a)