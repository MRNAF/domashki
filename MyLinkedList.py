class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None
class LinkedList:
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head is None
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                return
            current = current.next

    def insert_to_middle_before(self, target_data, data):
        new_node = Node(data)
        current = self.head
        while current:
            if current.data == target_data:
                if current.prev:
                    current.prev.next = new_node
                    new_node.prev = current.prev
                    new_node.next = current
                    current.prev = new_node
                else:
                    self.prepend(data)
                return
            current = current.next

    def insert_to_middle_after(self, target_data, data):
        new_node = Node(data)
        current = self.head
        while current:
            if current.data == target_data:
                if current.next:
                    current.next.prev = new_node
                    new_node.next = current.next
                    new_node.prev = current
                    current.next = new_node
                else:
                    self.append(data)
                return
            current = current.next


