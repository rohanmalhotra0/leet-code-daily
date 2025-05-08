class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False  # Negative numbers are not palindromes

        digits = []

        # Break x into digits
        temp = x  # store original
        while temp > 0:
            digits.insert(0, temp % 10)
            temp //= 10

        # Check if list is a palindrome
        for i in range(len(digits) // 2):
            if digits[i] != digits[-(i + 1)]:
                return False

        return True

# Example usage:
if __name__ == "__main__":
    x = 121
    solution = Solution()
    result = solution.isPalindrome(x)
    print(result)  # Output: True
# This will print True because 121 is a palindrome.


#  my solution 1150 / 1156 passed
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        bool = False
        digits = []
        if (x == 0):
        
            bool = True
            return bool
        
        while x > 0:
            digits.insert(0, x % 10)
            x //= 10

        for i in range(len(digits)):
            for j in range(len(digits) -1, -1, -1):
                nums1 = digits[j]
                nums = digits[i]
                if nums1 == nums:
                    bool = True
                else:
                    bool = False
        
        return bool
        '''
        
        def isPalindrome(self, x: int) -> bool:
            return str(x) == str(x)[::-1]
        # Example usage:
        if __name__ == "__main__":
            x = 121
            solution = Solution()
            result = solution.isPalindrome(x)
            print(result)  # Output: True
# This will print True because 121 is a palindrome.
# This will print True because 121 is a palindrome.
# This will print True because 121 is a palindrome.
# This will print True because 121 is a palindrome.
# This will print True because 121 is a palindrome.