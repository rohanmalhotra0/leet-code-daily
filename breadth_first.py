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