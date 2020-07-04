class Solution:
    def shuffle(self, nums: list, n: int) -> list:
        new_list = []
        for i in range(n):
            # print(nums[i])
            new_list.append(nums[i])

        for i in range(n):
            # 插入index 1,3,5,7... 0123 1357
            inx = i + (i + 1)
            new_list.insert(inx, nums[n+i])
        return new_list

r = Solution().shuffle([1,2,3,4,4,3,2,1], 4)
print(r)
