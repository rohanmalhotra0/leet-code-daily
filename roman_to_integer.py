class Solution:
    def romanToInt(self, s: str) -> int:
        
        sum = 0
        apple = {
        
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000

        }
        arr = list(s)
        
        for i in range (len(arr)):
            if (apple[arr[i]].appened(apple[arr[i - 1]]) == "IV"):
                sum += 4
            if (apple[arr[i]].appened(apple[arr[i - 1]]) == "IX"):
                sum += 9
            if (apple[arr[i]].appened(apple[arr[i - 1]]) == "XL"):
                sum += 40
            if (apple[arr[i]].appened(apple[arr[i - 1]]) == "XC"):
                sum += 90
            if (apple[arr[i]].appened(apple[arr[i - 1]]) == "CD"):
                sum += 400
            if (apple[arr[i]].appened(apple[arr[i - 1]]) == "CM"):
                sum += 900
            if (i == 0):
                sum += apple[arr[i]]
            else:
                sum += apple[arr[i]]

        return sum

def main():
    s = "MCMXCIV"
    solution = Solution()
    result = solution.romanToInt(s)
    print(f"The integer value of the Roman numeral {s} is: {result}")
    