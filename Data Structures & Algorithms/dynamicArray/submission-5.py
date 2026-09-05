class DynamicArray:
    
    def __init__(self, capacity: int):
        self.length = 0
        self.capacity = capacity or 0
        if capacity > 0:
            self.dynamicArr = [0] * capacity
        else:
            self.dynamicArr = []
        


    def get(self, i: int) -> int:
        return self.dynamicArr[i]


    def set(self, i: int, n: int) -> None:
        self.dynamicArr[i] = n

    def pushback(self, n: int) -> None:
        if self.length < self.capacity:
            self.dynamicArr[self.length] = n
            self.length += 1
        else:
            self.resize()
            self.dynamicArr[self.length] = n
            self.length += 1
        


    def popback(self) -> int:
        if self.length > 0:
            self.length -= 1
        return self.dynamicArr.pop(self.length)

    def resize(self) -> None:
        newArr = [None] * self.capacity
        self.dynamicArr.extend(newArr)
        self.capacity *= 2


    def getSize(self) -> int:
        return self.length

    def getCapacity(self) -> int:
        return self.capacity