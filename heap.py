class MinHeap:
    def __init__(self):
        self.heap = []

    def get_parent_index(self, index):
        return (index - 1) // 2
    
    def get_left_child_index(self, index):
        return 2 * index + 1

    def get_right_child_index(self, index):
        return 2 * index + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        while index > 0:
            parent_index = self.get_parent_index(index)
            if self.heap[index] < self.heap[parent_index]:
                self.swap(index, parent_index)
                index = parent_index
            else:
                break

    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return min_val

    def _heapify_down(self, index):
        while self.get_left_child_index(index) < len(self.heap):
            smallest = index
            left = self.get_left_child_index(index)
            right = self.get_right_child_index(index)

            if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != index:
                self.swap(index, smallest)
                index = smallest
            else:
                break

    def peek(self):
        return self.heap[0] if self.heap else None

    def __str__(self):
        return str(self.heap)

heap = MinHeap()
heap.insert(10)
heap.insert(5)
heap.insert(14)
heap.insert(1)

print("Heap:", heap)           # [1, 5, 14, 10]
print("Min:", heap.peek())    # 1

print("Extracted:", heap.extract_min())  # 1
print("Heap after extraction:", heap)    # [5, 10, 14]
