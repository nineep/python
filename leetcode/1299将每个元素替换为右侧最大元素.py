class Solution:
    def replaceElements(self, arr: list) -> list:
        if 1 <= len(arr) <= 10**4 and max(arr) <= 10**5:
            ls = arr
            for i in range(len(arr)):
                value = 0
                for ii in range(len(arr)):
                    if ii > i and arr[ii] > value:
                        value = arr[ii]
                        ls[i] = value
                        print(ls)
            ls[-1] = -1
            return ls


a = Solution().replaceElements([17,18,5,4,6,1])
print(a)
