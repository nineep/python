class Solution:
    """
    0123 0123456
    0123 123456
    0123 23456
    0123 3456

    """
    def strStr(self, haystack: str, needle: str) -> int:
        a = haystack
        b = needle
        # 最多能尝试匹配的次数循环
        for n in range(len(a) - len(b)):
            print('**开始第', n, '种匹配')

            for m in range(len(b)):
                if b[m] == a[m+n]:
                    print('第', m+1, '个元素相同')
                    if m+1 == len(b):
                        print('第', n, '位匹配成功')
                        return n
                else:
                    print('第', m+1, '个元素不相同，结束此种匹配')
                    break
        else:
            return -1

t = Solution().strStr('nineep', 'nineep')
print(t)
