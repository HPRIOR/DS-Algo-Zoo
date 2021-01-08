class Heap:
    def __init__(self):
        self.items = []

    def get_left_child_index(self, parent_index):
        return (parent_index * 2) + 1

    def get_right_child_index(self, parent_index):
        return (parent_index * 2) + 2

    def get_parent_index(self, child_index):
        return (child_index - 1) / 2

    # checking for left and right children requires a check that the index produced
    # by mathematics to get indexes is within the bounds of the array or in the case
    # getting the parent, it is >= 0
    def has_left_child(self, index):
        return self.get_left_child_index(index) < len(self.items)

    def has_right_child(self, index):
        return self.get_right_child_index(index) < len(self.items)

    def has_parent(self, index):
        return self.get_parent_index(index) >= 0

    def left_child(self, index):
        return self.items[self.get_left_child_index(index)]

    def right_child(self, index):
        return self.items[self.get_right_child_index(index)]

    def parent(self, index):
        return self.items[self.get_parent_index(index)]

    def swap(self, index_1, index_2):
        temp = self.items[index_1]
        self.items[index_1] = index_2
        self.items[index_2] = temp

    def peak(self):
        if len(self.items) == 0:
            raise IndexError()
        return self.items[0]

    def pop(self):
        if len(self.items) == 0:
            raise IndexError()
        item = self.items[0]
        self.items[0] = self.items[-1]
        self.items.pop()
        self.reheap_down()
        return item

    def add(self, item):
        self.items.append(item)
        self.reheap_up()

    def reheap_up(self):
        index = len(self.items) - 1
        while self.has_parent(index) and self.parent(index) > self.items[index]:
            self.swap(self.get_parent_index(index), index)
            index = self.get_parent_index(index)

    def reheap_down(self):
        index = 0
        while self.has_left_child(index):
            smaller_child_index = self.get_left_child_index(index)
            if self.has_right_child(index) and self.right_child(index) < self.left_child(index):
                smaller_child_index = self.get_right_child_index(index)

            if self.items[index] < self.items[smaller_child_index]:
                break
            else:
                self.swap(index, smaller_child_index)
            index = smaller_child_index
