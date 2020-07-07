class Solution:
    def createTargetArray(self, nums: list, index: list) -> list:
        target_list = []
        for i in range(len(nums)):
            nums_value = nums[i]
            index_value = index[i]
            target_list.insert(index_value, nums_value)
        return target_list


a = Solution().createTargetArray([0,1,2,3,4], [0,1,2,2,1])
print(a)