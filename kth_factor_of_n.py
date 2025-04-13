class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        tomas = []
        for i in range (n + 1):
            if (i != 0 and n % i == 0):
                tomas.append(i)
        print(tomas)
        if (len(tomas) == k):
            return tomas[k - 1]
        if (len(tomas) == 1 and k == 1):
            return tomas[0]
        if (len(tomas) > k):
            return tomas[k - 1]
        else:
            return -1

# Example usage:
solution = Solution()
print(solution.kthFactor(12, 3))  # Output: 3
print(solution.kthFactor(7, 2))   # Output: -1
# Test cases
print(solution.kthFactor(1, 1))   # Output: 1

'''
You are given two positive integers n and k. A factor of an integer n is defined as an integer i where n % i == 0.

Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or return -1 if n has less than k factors.

 

Example 1:

Input: n = 12, k = 3
Output: 3
Explanation: Factors list is [1, 2, 3, 4, 6, 12], the 3rd factor is 3.
Example 2:

Input: n = 7, k = 2
Output: 7
Explanation: Factors list is [1, 7], the 2nd factor is 7.
Example 3:

Input: n = 4, k = 4
Output: -1
Explanation: Factors list is [1, 2, 4], there is only 3 factors. We should return -1.
 

Constraints:

1 <= k <= n <= 1000
 

Follow up:

Could you solve this problem in less than O(n) complexity?



'''


'''
What worked for me was writing everything out and using print statements and the output to debug my code. First almost pure problem solved in leetcode
'''

def kthFactor(n: int, k: int) -> int:
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    if k <= len(factors):
        return factors[k - 1]
    else:
        return -1
# Example usage
print(kthFactor(12, 3))  # Output: 3

print(kthFactor(7, 2))   # Output: 7
print(kthFactor(4, 4))   # Output: -1
# Test cases
print(kthFactor(1, 1))   # Output: 1
print(kthFactor(1000, 10))  # Output: 10
print(kthFactor(1000, 20))  # Output: 20

print(kthFactor(1000, 30))  # Output: 30

def kthFactor(n: int, k: int) -> int:
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    if k <= len(factors):
        return factors[k - 1]
    else:
        return -1