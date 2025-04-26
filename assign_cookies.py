class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        maxCount = 0
        size = len(s)
        g.sort() 
        s.sort()
        for i in range(len(g)):
            for j in range(len(s)):
                if s[j] >= g[i]:
                    maxCount += 1
                    break
        if maxCount > size:
            return size            
        return maxCount 
    
    '''
    class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        content_children = 0
        cookie_index = 0
        while cookie_index < len(s) and content_children < len(g):
            if s[cookie_index] >= g[content_children]:
                content_children += 1
            cookie_index += 1
        return content_children
    
    '''