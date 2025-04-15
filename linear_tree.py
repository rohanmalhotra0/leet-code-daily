def linear_tree(n):
    """
    Generate a linear tree structure with n nodes.

    Args:
        n (int): Number of nodes in the tree.

    Returns:
        list: A list of tuples representing the edges of the tree.
    """
    if n < 1:
        return []

    edges = []
    for i in range(1, n):
        edges.append((i, i + 1))
    
    return edges
# Example usage:
if __name__ == "__main__":
    n = 5
    tree = linear_tree(n)
    print("Linear tree edges:", tree)
    # Output: Linear tree edges: [(1, 2), (2, 3), (3, 4), (4, 5)]
# This will print the edges of a linear tree with 5 nodes.
# A linear tree is a tree where each node has at most one child.