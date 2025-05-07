from collections import defaultdict
from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        count = defaultdict(int)
        cur_sum = 0
        left = 0

        for right in range(len(nums)):
            # include nums[right]
            cur_sum += nums[right]
            count[nums[right]] += 1

            # if window grows too big, pop from left
            if right - left + 1 > k:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]]
                cur_sum -= nums[left]
                left += 1

            # if window is size k and all k are distinct
            if right - left + 1 == k and len(count) == k:
                res = max(res, cur_sum)

        return res
    
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        count = defaultdict(int)
        cur_sum = 0
        left = 0

        for right in range(len(nums)):
            # include nums[right]
            cur_sum += nums[right]
            count[nums[right]] += 1

            # if window grows too big, pop from left
            if right - left + 1 > k:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]]
                cur_sum -= nums[left]
                left += 1

            # if window is size k and all k are distinct
            if right - left + 1 == k and len(count) == k:
                res = max(res, cur_sum)

        return res
#     print("Depth First Search starting from vertex A:")
#     depth_first_search(graph, 'A')
# # Output: A B D E C F
# # This will print the nodes in the order they are visited.
# # This is a simple implementation of the depth-first search (DFS) algorithm.
#
# Example usage:
if __name__ == "__main__":
    # Graph represented as an adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    print("\nDepth First Search starting from vertex A:")
    depth_first_search(graph, 'A')

    def dfs (graph, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=' ')
        for neighbor in graph[start]:
            if neighbor not in visited:
                dfs(graph, neighbor, visited)
        return visited
    # Example usage:
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }