class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = "".join(sorted(s))
        s1 = s1.lower()
        s1 = s1.replace(" ", "")
        s1 = s1.replace("?", "")
        print(s1)
        for i in range(1, len(s1)):
            if (s1[i] != s1[i-1]):
                return False
        return True