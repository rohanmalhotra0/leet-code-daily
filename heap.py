def heap() -> list:
    """
    This function creates a heap data structure. It initializes an empty list to represent the heap.
    """
    
    heap = []  # Initialize an empty list to represent the heap
    
    return heap
def heapImplementation():
    """
    This function demonstrates the implementation of a heap data structure.
    It initializes an empty list to represent the heap and provides methods to insert elements and maintain the heap property.
    """
    
    heap = []  # Initialize an empty list to represent the heap
    
    def insert(value):
        """
        Inserts a value into the heap and maintains the heap property.
        """
        heap.append(value)  # Add the new value to the end of the list
        _heapify_up(len(heap) - 1)  # Restore the heap property by moving the new value up
    
    def _heapify_up(index):
        """
        Moves the value at the given index up to restore the heap property.
        """
        parent_index = (index - 1) // 2  # Calculate the index of the parent node
        if index > 0 and heap[index] < heap[parent_index]:
            heap[index], heap[parent_index] = heap[parent_index], heap[index]
            _heapify_up(parent_index)

#example usage
    insert(10)
    insert(5)
    insert(20)
    insert(15)
    print(heap)  # Output: [5, 10, 20, 15]
    
    return heap
# This will print the heap after inserting the values.
 