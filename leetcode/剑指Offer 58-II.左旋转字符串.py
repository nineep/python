class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        new_str1 = ''
        new_str2 = ''
        for i in range(len(s)):
            if i < n:
                new_str2 += s[i]
            else:
                new_str1 += s[i]
        return new_str1+new_str2


a = Solution().reverseLeftWords('abcdefg', 2)
print(a)