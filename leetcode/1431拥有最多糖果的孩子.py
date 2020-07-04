class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        new_candies = []
        for i in range(len(candies)):
            new = candies[i] + extraCandies
            new_candies.append(new)

        r_list = []
        for n in new_candies:
            r = 'true'
            print('加后值', n)
            print('-----------')
            for m in candies:
                print('对比值', m)
                if n >= m:
                    print('大于等于，为最大值')
                else:
                    print('小于，不是最大值')
                    r = 'false'
            r_list.append(r)
        print(r_list)
        return r_list

        # for n in candies:
        #     print('n', n)
        #     new_n = n + extraCandies
        #     print(new_n)
        #     new_list = []
        #     for i in range(len(candies)):
        #         if new_n >= candies[i]:
        #             new_list.append('true')
        #             print(new_list)
        #         else:
        #             new_list.append('false')
        #             print(new_list)
        # return new_list

a = Solution().kidsWithCandies([2,3,5,1,3], 3)
print(a)
