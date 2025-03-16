class Solution:
    def intToRoman(self, num: int) -> str:
        dividers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        Symbols  = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        roman = ''

        def max_divisor(n):
            for index,i in enumerate(dividers):
                if n >= i:
                    return index
                    break
                else:
                    continue
    
        while num>0:
            index_of_max_divisor = max_divisor(num)
            times = num//dividers[index_of_max_divisor]
            roman = roman + str(Symbols[index_of_max_divisor])*times
            num = num % dividers[index_of_max_divisor]

        return roman
