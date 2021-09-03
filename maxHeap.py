import sys 
  
class MaxHeap: 
  
    def __init__(self, maxsize): 
        self.maxsize = maxsize 
        self.size = 0
        self.Heap = [0]*(self.maxsize + 1) 
        self.Heap[0] = sys.maxsize 
        self.FRONT = 1
  
    def parent(self, pos): 
        return pos // 2
  
    def leftChild(self, pos): 
        return 2 * pos 
  
    def rightChild(self, pos): 
        return (2 * pos) + 1
  
    def isLeaf(self, pos): 
        if pos >= (self.size//2) and pos <= self.size: 
            return True
        return False
  
    
    # Function to heapify the node at pos 
    def maxHeapify(self, pos): 
  
        if not self.isLeaf(pos): 
            if (self.Heap[pos] < self.Heap[self.leftChild(pos)] or
                self.Heap[pos] < self.Heap[self.rightChild(pos)]): 
  
                if self.Heap[self.leftChild(pos)] > self.Heap[self.rightChild(pos)]: 
                    self.Heap[pos], self.Heap[self.leftChild(pos)] = self.Heap[self.leftChild(pos)], self.Heap[pos] 
                    self.maxHeapify(self.leftChild(pos)) 
  
                else: 
                    self.Heap[pos], self.Heap[self.rightChild(pos)] = self.Heap[self.rightChild(pos)], self.Heap[pos] 
                    self.maxHeapify(self.rightChild(pos)) 
  
    # Function to insert a node into the heap 
    def insert(self, element): 
        if self.size >= self.maxsize : 
            return
        self.size+= 1
        self.Heap[self.size] = element 
  
        current = self.size 
  
        while self.Heap[current] > self.Heap[self.parent(current)]: 
            self.Heap[current], self.Heap[self.parent(current)] = self.Heap[self.parent(current)],self.Heap[current]  
            current = self.parent(current) 
    
    def popMax(self): 
        popped = self.Heap[self.FRONT] 
        self.Heap[self.FRONT] = self.Heap[self.size] 
        self.size-= 1
        self.maxHeapify(self.FRONT) 
        return popped 
  
