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
