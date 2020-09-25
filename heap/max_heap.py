class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        for i in range(len(self.storage)):
            try:
                self._sift_down(i)
            except IndexError:
                pass
        for i in range(len(self.storage)-1, 0,-1):
            try:
                self._bubble_up(i)
            except IndexError:
                pass


    def delete(self):
        return self.storage.pop(0)

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        parent_index = (index - 1) // 2
        parent_value = self.storage[parent_index]
        if self.storage[index] > self.storage[parent_index]:
            self.storage[parent_index] = self.storage[index]
            self.storage[index] = parent_value

    def _sift_down(self, index):
        child_index1 = 2 * index + 1
        child_index2 = 2 * index + 2
        big_child = max(self.storage[child_index1], self.storage[child_index2])
        big_child_index = self.storage.index(big_child)
        if big_child > self.storage[index]:
            self.storage[big_child_index] = self.storage[index]
            self.storage[index] = big_child