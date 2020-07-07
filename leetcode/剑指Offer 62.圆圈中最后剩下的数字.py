class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        """
        """
        ls = []
        for num in range(n):
            ls.append(num)
        print('ls', ls)

        index_offset = 0
        print('初始index offset', index_offset)
        while len(ls) > 1:
            # index每次偏移2，即到第三个元素
            index_offset += (m-1)
            print('--------------------------')
            print('往后数', m-1, 'index offset:', index_offset)

            if index_offset < len(ls):
                print('此次遍历中可直接删除')

            else:
                print('offset溢出列表，需要在下次遍历中定位元素再删除')

                # index_offset小于等于len(ls)，否者一直循环减len(ls)
                while index_offset >= len(ls):
                    index_offset -= len(ls)

                print('减后', index_offset)
                index_offset = abs(index_offset)

            print('delete index offset', index_offset)
            ls.pop(index_offset)
            print('ls:', ls, '长度：', len(ls))

        return ls[0]


a = Solution().lastRemaining(9, 13)
print(a)
