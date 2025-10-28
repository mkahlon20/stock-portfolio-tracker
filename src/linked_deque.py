class DLNode:
    def __init__(self, previous_node=None, data_portion=None, next_node=None):
        self.data = data_portion
        self.next = next_node
        self.prev = previous_node

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_next_node(self):
        return self.next

    def set_next_node(self, next_node):
        self.next = next_node

    def get_previous_node(self):
        return self.prev

    def set_previous_node(self, previous_node):
        self.prev = previous_node


class LinkedDeque:
    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0
        
    def __iter__(self):
        """Make LinkedDeque iterable for use in for loops"""
        current = self.front
        while current:
            yield current.data
            current = current.next

    def is_empty(self):
        return self.size == 0

    def add_to_front(self, new_entry):
        new_node = DLNode(None, new_entry, self.front)
        if self.is_empty():
            self.back = new_node
        else:
            self.front.set_previous_node(new_node)
        self.front = new_node
        self.size += 1

    def add_to_back(self, new_entry):
        new_node = DLNode(self.back, new_entry, None)
        if self.is_empty():
            self.front = new_node
        else:
            self.back.set_next_node(new_node)
        self.back = new_node
        self.size += 1

    def get_front(self):
        if self.is_empty():
            return None
        return self.front.get_data()

    def get_back(self):
        if self.is_empty():
            return None
        return self.back.get_data()

    def remove_front(self):
        if self.is_empty():
            return None
        removed_data = self.front.get_data()
        self.front = self.front.get_next_node()
        self.size -= 1
        if self.front is None:
            self.back = None
        else:
            self.front.set_previous_node(None)
        return removed_data

    def remove_back(self):
        if self.is_empty():
            return None
        removed_data = self.back.get_data()
        self.back = self.back.get_previous_node()
        self.size -= 1
        if self.back is None:
            self.front = None
        else:
            self.back.set_next_node(None)
        return removed_data

    def clear(self):
        self.front = None
        self.back = None
        self.size = 0

    def display(self):
        current = self.front
        result = []
        while current:
            result.append(str(current.get_data()))
            current = current.get_next_node()
        return " -> ".join(result)
        self.front = None
        self.back = None
        self.size = 0

    def display(self):
        current = self.front
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements)
    