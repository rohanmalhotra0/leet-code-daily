class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1 
        if x == 2:
            return 1
        for i in range (x):
            if i * i > x:
                return i - 1
        return 0 
    
    def mySqrt2(self, x: int) -> int:
        while x > 0:
            if x * x > x:
                return x - 1
            else:
                return x
        return 0
    