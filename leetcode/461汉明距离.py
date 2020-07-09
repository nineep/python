class Solution:
    def hammingDistance(self, x:int, y:int) -> int:

        if x > y:
            str_x = bin(x).lstrip('0b')
            str_y = bin(y).lstrip('0b').rjust(len(str_x), '0')

        else:
            str_y = bin(y).lstrip('0b')
            str_x = bin(x).lstrip('0b').rjust(len(str_y), '0')

        count = 0
        for i in range(len(str_x)):
            if str_x[i] == str_y[i]:
                pass
            else:
                count += 1

        return count


a = Solution().hammingDistance(93, 23)
print(a)