class Solution:
    def decompressRLElist(self, nums: list) -> list:
        result_list = []
        for i in range(len(nums) // 2):
            freq, val = nums[2*i], nums[2*i+1]
            while freq > 0:
                result_list.append(val)
                freq -= 1
        return result_list


a = Solution().decompressRLElist([1, 2, 3, 4])
print(a)