class Node:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, nim, nama):
        new_node = Node(nim, nama)
        if not self.head:  # Jika list kosong
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def pop(self):
        if not self.tail:  # Jika list kosong
            return None
        popped_node = self.tail
        if self.tail.prev:  # Jika ada lebih dari satu node
            self.tail = self.tail.prev
            self.tail.next = None
        else:  # Jika hanya ada satu node
            self.head = None
            self.tail = None
        return popped_node

    def prepend(self, nim, nama):
        new_node = Node(nim, nama)
        if not self.head:  # Jika list kosong
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert(self, index, nim, nama):
        new_node = Node(nim, nama)
        if index == 0:
            self.prepend(nim, nama)
            return
        current = self.head
        for i in range(index):
            if current is None:
                raise IndexError("Index out of bounds")
            current = current.next
        if current is None:  # Jika index lebih besar dari jumlah node
            self.append(nim, nama)
        else:
            new_node.prev = current.prev
            new_node.next = current
            if current.prev:
                current.prev.next = new_node
            current.prev = new_node
            if new_node.prev is None:  # Jika menambahkan di depan
                self.head = new_node

    def remove(self, nim):
        current = self.head
        while current:
            if current.nim == nim:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:  # Jika node yang dihapus adalah head
                    self.head = current.next
                if current == self.tail:  # Jika node yang dihapus adalah tail
                    self.tail = current.prev
                return current
            current = current.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(f"NIM: {current.nim}, Nama: {current.nama}")
            current = current.next

# Contoh penggunaan
dll = DoubleLinkedList()
dll.append("001", "Fahrel")
dll.append("002", "Ilham")
dll.prepend("003", "Jaya")
dll.insert(1, "004", "Kusuma")

print("List setelah append, prepend, dan insert:")
dll.print_list()

popped_node = dll.pop()
print(f"\nPopped node: NIM: {popped_node.nim}, Nama: {popped_node.nama}")

print("\nList setelah pop:")
dll.print_list()

removed_node = dll.remove("222222")
if removed_node:
    print(f"\nRemoved node: NIM: {removed_node.nim}, Nama: {removed_node.nama}")

print("\nList setelah remove:")
dll.print_list()