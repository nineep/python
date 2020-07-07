class Solution:
    def findNumbers(self, nums: list) -> int:
        count = 0
        for n in nums:
            if (len(str(n)) % 2) == 0:
                count += 1
        return count


a = Solution().findNumbers([12,345,2,6,7896])
print(a)
