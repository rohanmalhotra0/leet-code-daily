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
                sum += 9
            else:
                sum += apple[arr[i]]

        return sum
