class Solution:
    def smallerNumbersThanCurrent(self, nums: list) -> list:
        out_list = []
        for i in range(len(nums)):
            count = 0
            for ii in range(len(nums)):
                if ii != i and nums[ii] < nums[i]:
                    count += 1
            out_list.append(count)
        return out_list


a = Solution().smallerNumbersThanCurrent([8,1,2,2,3])
print(a)