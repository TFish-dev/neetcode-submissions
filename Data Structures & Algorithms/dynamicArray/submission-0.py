class DynamicArray:
    
    def __init__(self, capacity: int):
        if capacity <= 0:
            self.capacity = 0
        self.capacity = capacity
        self.size = 0
        self.arr = [None] * (self.capacity)


    def get(self, i: int) -> int:
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        self.arr[i] = n


    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        index = self.capacity - 1
        for v in self.arr[::-1]:
            if self.arr[index] != None:
                self.arr[index] = None
                self.size -= 1
                return v
            index -= 1

    def resize(self) -> None:
        self.capacity *= 2
        newArr = [None] * self.capacity
        idx = 0
        for v in self.arr:
            newArr[idx] = v
            idx += 1
        self.arr = newArr

    def getSize(self) -> int:
        return self.size        
    
    def getCapacity(self) -> int:
        return self.capacity
