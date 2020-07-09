class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        """
        假设 出现一次 (为 +1， 出现一次 )为 -1,
        遍历，值相加，直到为 0，则可去掉外围括号
        """
        new_s_ls = list(S)
        index_ls = [0]
        count = 0

        for i in range(len(S)):
            if S[i] == '(':
                count += 1
            else:
                count -= 1

            if count == 0:
                index_ls.append(i)
                if i < (len(S) - 1):
                    index_ls.append(i+1)

        for idx in index_ls:
            new_s_ls[idx] = ''

        new_str = ''
        for n in new_s_ls:
            new_str += n
        return new_str


a = Solution().removeOuterParentheses("(()())(())(()(()))")
print(a)
