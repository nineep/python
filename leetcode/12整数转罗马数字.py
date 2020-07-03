class Solution:
    def intToRoman(self, num: int) -> str:
        roman_str = ''
        for i, n in enumerate(str(num)):
            index_max = len(str(num))
            i = index_max - i

            if i == 1:
                roman = self.bitToRoman(n)
            elif i == 2:
                roman = self.bitToRoman(n, one='X', five='L', ten='C')
            elif i == 3:
                roman = self.bitToRoman(n, one='C', five='D', ten='M')
            else:
                roman = self.bitToRoman(n, one='M')

            roman_str += roman
        print(roman_str)
            # if int(n) < 4:
            #     print('I'*int(n))
            # elif int(n) == 4:
            #     print('IV')
            # elif int(n) == 5:
            #     print('V')
            # elif int(n) == 9:
            #     print('IX')
            # else:
            #     print('X'+'I'*(int(n)-5))

    def bitToRoman(self, n: str, one='I', five='V', ten='X'):
        """
        默认n是个位数， 1<n<3999
        个位： IVX
        十位： XLC
        百位： CDM
        千位： M
        """
        if int(n) < 4:
            print(one * int(n))
            roman = one * int(n)
        elif int(n) == 4:
            print(one+five)
            roman = one+five
        elif int(n) == 5:
            print(five)
            roman = five
        elif int(n) == 9:
            print(one+ten)
            roman = one + ten
        else:
            print(five + one * (int(n) - 5))
            roman = five + one * (int(n) - 5)
        return roman

r = Solution().intToRoman(58)
# r = Solution().bitToRoman('7')
# print(r)