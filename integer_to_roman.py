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
    
# The code defines a class `Solution` with a method `intToRoman` that converts an integer to its Roman numeral representation.
# The method uses two lists: `val` for integer values and `syms` for corresponding Roman symbols.
# It iterates through the `val` list, subtracting the integer value from `num` and appending the corresponding Roman symbol to `roman_num`.
# The process continues until `num` is reduced to zero.
# The example usage demonstrates how to create an instance of the `Solution` class and call the `intToRoman` method with an integer input.
# The output is printed to the console.
# The code is efficient and handles the conversion in a straightforward manner.
def test_int_to_roman():
    solution = Solution()
    assert solution.intToRoman(1) == "I"
    assert solution.intToRoman(4) == "IV"
    assert solution.intToRoman(9) == "IX"
    assert solution.intToRoman(58) == "LVIII"
    assert solution.intToRoman(1994) == "MCMXCIV"
    print("All tests passed.")