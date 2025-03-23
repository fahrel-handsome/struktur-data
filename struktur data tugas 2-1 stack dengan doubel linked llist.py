#stack dengan double linked list
class Dnode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class StackDoubleLinkedList:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None
    
    def push(self, item):
        new_node = Dnode(item)
        if self.top:
            new_node.prev = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            print("Stack Kosong!") 
            return None
        item = self.top.data
        self.top = self.top.prev
        return item
    def peek(self):
        if self.is_empty():
            return None
        return self.top.data
    
stack = StackDoubleLinkedList()
print("\ninput 1:")
print("[100, 200, 300]")
stack.push(100)
stack.push(200)
stack.push(300)

print("Top dalam stack sebelum pop:", stack.peek())
print("pop:", stack.pop ())
print("pop:", stack.pop ())
print("top dalam stack setelah pop:", stack.peek())

print("\ninput 2")
print("[50, 150, 250, 350]")
stack.push(50)
stack.push(150)
stack.push(250)
stack.push(350)

print("Top dalam stack sebelum pop:", stack.peek())
print("pop:", stack.pop ())
print("top dalam stack setelah pop:", stack.peek())


