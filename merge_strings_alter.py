class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        full = []
        word1s = [word1]
        word2s = [word2]
        count = 0
        even = 0
        big = 0
        small = 0
        if (word1 >= word2):
            count = len(word1)
        else:
            count = len(word2) 

        if (word1 >= word2):
            big = len(word1)
        else:
            small = len(word2) 

        
        for i in range (count):
            if (even == 0):
                full.append(word1s[i])
                even = even + 1
            elif (even == 1):
                full.append(word1s[i])
                even = even - 1
