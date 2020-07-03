import time

class Solution:
    def longestCommonPrefix(self, strs):
        start_index = 0
        while True:

            ls = []
            for i in strs:
                ls.append(i[start_index])

            print(ls, set(ls))

            if len(set(ls)) == 1:
                print('第', start_index, ' index same letters')

            else:
                print('different letters')
                print('字母不同的索引为：', start_index)
                break

            start_index += 1

        if start_index == 0:
            print('无相同')
            return 0

        else:
            return strs[0][0:start_index]

        # for i, s in enumerate(strs):
        #     ls = []
        #     for ss in s:
        #         ls.append(ss)
        #
        #     new_dict = {i: ls}
        #     # print("new_dict", new_dict)
        #
        #     d.update(new_dict)
        #
        # # for dict_element_num in range(len(d)):
        # #     ls_element_index = 1
        # #     print('dict_element_num', dict_element_num)
        # #     print(d[dict_element_num][0], d[dict_element_num][ls_element_index])
        # #     while d[dict_element_num][0] == d[dict_element_num][ls_element_index]:
        # #         ls_element_index =+ 1
        # #         print(ls_element_index)
        #
        # # dict_len = len(d) - 1
        # switch = True
        # ls_index = 0
        #
        # while switch:
        #     dict_len = len(d) - 1
        #
        #     time.sleep(2)
        #     print('=======================')
        #     print('ls_index', ls_index)
        #     print('dict_len', dict_len)
        #     print('----------------------')
        #     while dict_len:
        #         print('dict_len', dict_len)
        #         if d[0][ls_index] == d[dict_len][ls_index]:
        #             print(d[0][ls_index], '和', d[dict_len][ls_index], '相等')
        #             dict_len -= 1
        #
        #         else:
        #             print(ls_index)
        #             switch = False
        #
        #     ls_index += 1
        #
        #
        #
        # return ls_index


ll = ["dog","doracecar","docar"]
r = Solution().longestCommonPrefix(ll)
print(r)