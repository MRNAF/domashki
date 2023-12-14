from MyLinkedList import LinkedList

class Queue:
    def __init__(self):
        self.linked_list = LinkedList()
    def IsEmpty(self):
        return self.linked_list.is_empty()
    def Enqueue(self, data):
        self.linked_list.append(data)
    def Dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return
        data = self.linked_list.head.data
        self.linked_list.delete(data)
        return data

    def Front(self):
        if self.is_empty():
            print("Queue is empty")
            return
        return self.linked_list.head.data

#Test
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.front()
queue.dequeue()

