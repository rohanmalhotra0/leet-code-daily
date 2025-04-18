class Solution:
    def intToRoman(self, num: int) -> str:
        # Define the mapping of integers to Roman numerals
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        
        roman_num = ''
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                roman_num += syms[i]
                num -= val[i]
            i += 1
        return roman_num
# # Example usage:
if __name__ == "__main__":
    solution = Solution()
    num = 1994
    result = solution.intToRoman(num)
    print(result)  # Output: "MCMXCIV"
    