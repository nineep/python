class Solution:
    def plusOne(self, digits: list) -> list:
        # digits[-1] = digits[-1] + 1
        # if digits[-1] == 10:
        #     digits[-1] = 1
        #     digits.append(0)
        # return digits

        num = ''
        for i in range(len(digits)):
            num += str(digits[i])

        new_num = int(num) + 1
        num_list = list(str(new_num))
        for i in range(len(num_list)):
            num_list[i] = int(num_list[i])

        return num_list

a = Solution().plusOne([1,2,9])
print(a)