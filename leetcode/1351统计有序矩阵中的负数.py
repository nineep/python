class Solution:
    def countNegatives(self, grid: list) -> int:
        count = 0
        for sub_ls in grid:
            for ls in sub_ls:
                if ls < 0:
                    count += 1
        return count


a = Solution().countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]])
print(a)