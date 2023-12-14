from MyLinkedList import LinkedList
class Stack:
    def __init__(self):
        self.linked_list = LinkedList()
    def IsEmpty(self):
        return self.linked_list.is_empty()
    def Push(self, data):
        self.linked_list.prepend(data)
    def Pop(self):
        if self.IsEmpty():
            print("Stack is empty")
            return
        data = self.linked_list.head.data
        self.linked_list.delete(data)
        return data
    def Top(self):
        if self.IsEmpty():
            raise ValueError("Stack is empty")
        return self.linked_list.head.data



#Test
stack = Stack()
stack.Pop()
stack.Push(1)
stack.Push(2)
stack.Push(3)
stack.Pop()
