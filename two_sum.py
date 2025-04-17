def two_sum(nums, target):
    seen = {}  # key: number, value: index

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    return []  # If no solution found


# What this does is:
# 1. It initializes an empty dictionary called `seen`.
# 2. It iterates through the list `nums` using `enumerate`, which gives both the index `i` and the number `num`.
# 3. For each number, it calculates its complement with respect to the target.
# 4. It checks if the complement is already in the `seen` dictionary.
# 5. If it is, it returns the indices of the complement and the current number.
# 6. If not, it adds the current number and its index to the `seen` dictionary.
# 7. If no solution is found, it returns an empty list.
# This algorithm runs in O(n) time complexity and uses O(n) space complexity.
# Example usage:
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print(result)  # Output: [0, 1]
# This will print the indices of the two numbers that add up to the target.
# This is a common problem in coding interviews and competitive programming.
# It is often referred to as the "Two Sum" problem.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node
        current = dummy
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next
# This code defines a function `addTwoNumbers` that takes two linked lists representing two non-negative integers and returns their sum as a linked list.
# The digits are stored in reverse order, meaning that the 1's digit is at the head of the list.
