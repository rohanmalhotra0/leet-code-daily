# adding all of alphabet in a map 
map1 = {i + 1: chr(ord('A') + i) for i in range(26)}

#binary search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
# sliding window example
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
     stored = set()
        left = 0
        maxLength = 0

        for right, ch in enumerate(s):
            # If ch is already in the window, shrink from the left
            while ch in stored:
                stored.remove(s[left])
                left += 1

            # Add the new character and update the maximum length
            stored.add(ch)
            currLength = right - left + 1
            maxLength = max(maxLength, currLength)

        return maxLength
# Example usage
s = "abcabcbb"
solution = Solution()
result = solution.lengthOfLongestSubstring(s)
print(f"The length of the longest substring without repeating characters in '{s}' is: {result}")
# Example usage of binary search
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
result = binary_search(arr, target)
if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the array.")
# Example usage of map1
for key, value in map1.items():
    print(f"{key}: {value}")
# Example usage of binary search
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
result = binary_search(arr, target)
if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the array.")
    
