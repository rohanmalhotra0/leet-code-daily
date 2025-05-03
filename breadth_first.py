def breadth_first_search(graph, start):
    visited = set()  # Set to keep track of visited nodes
    queue = []  # Initialize a queue

    # Start with the first node
    queue.append(start)
    visited.add(start)

    while queue:
        # Dequeue a vertex from the queue and print it
        vertex = queue.pop(0)
        print(vertex, end=" ")

        # Get all adjacent vertices of the dequeued vertex
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                
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

    print("Breadth First Search starting from vertex A:")
    breadth_first_search(graph, 'A')
# Output: A B C D E F
# This will print the nodes in the order they are visited.
# This is a simple implementation of the breadth-first search (BFS) algorithm.


#dfs
def depth_first_search(graph, start, visited=None):
    if visited is None:
        visited = set()  # Initialize the visited set if not provided

    visited.add(start)  # Mark the current node as visited
    print(start, end=" ")  # Print the current node

    # Recur for all the vertices adjacent to this vertex
    for neighbor in graph[start]:
        if neighbor not in visited:
            depth_first_search(graph, neighbor, visited)
            
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
       trips = [[]]
       currTrips = []
       L , R = 0 , 2
       while R < len(nums) - 1:
            if R - L + 1 > 3:
                currTrips.remove(nums[L])
                L += 1
            currTrips += nums[R]
            R -= 1         
       return trips 