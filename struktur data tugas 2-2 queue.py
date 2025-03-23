#2A queue araay
# class QueueArray:
#     def __init__(self, capacity):
#         self.queue = [None] * capacity  # Inisialisasi array dengan None
#         self.capacity = capacity
#         self.front = 0
#         self.rear = -1
#         self.count = 0

#     def enqueue(self, item):
#         if self.count == self.capacity:
#             print("Queue penuh!")
#             return
        
#         self.rear = (self.rear + 1) % self.capacity
#         self.queue[self.rear] = item
#         self.count += 1
#         self.display(f"setelah nilai {item} masuk")

#     def dequeue(self):
#         if self.count == 0:
#             print("Queue kosong!")
#             return None
        
#         removed_item = self.queue[self.front]
#         self.queue[self.front] = None
#         self.front = (self.front + 1) % self.capacity
#         self.count -= 1
#         self.display(f"setelah nilai {removed_item} keluar")
#         return removed_item
    
#     def display(self, message):
#         print(f"{message}  --> {self.queue}")

# # Uji dengan input pertama dan kedua
# queue1 = QueueArray(5)
# queue2 = QueueArray(6)

# print("\n================Queue Biasa dengan Array #1==================")
# for num in [10, 20, 30, 40, 50]:
#     queue1.enqueue(num)
# queue1.dequeue()
# queue1.dequeue()

# print("\n================Queue Biasa dengan Array #2==================")
# for num in [5, 15, 25, 35, 45, 55]:
#     queue2.enqueue(num)
# queue2.dequeue()
# queue2.dequeue()





#2B queue circular
# class CircularQueue:
#     def __init__(self, capacity):
#         self.queue = [None] * capacity
#         self.capacity = capacity
#         self.front = -1
#         self.rear = -1

#     def is_full(self):
#         return (self.rear + 1) % self.capacity == self.front

#     def is_empty(self):
#         return self.front == -1

#     def enqueue(self, item):
#         if self.is_full():
#             print(f"Queue penuh! Tidak bisa menambahkan {item}")
#             return
        
#         if self.is_empty():
#             self.front = 0
        
#         self.rear = (self.rear + 1) % self.capacity
#         self.queue[self.rear] = item
#         self.display(f"setelah nilai {item} masuk")

#     def dequeue(self):
#         if self.is_empty():
#             print("Queue kosong! Tidak bisa melakukan dequeue")
#             return None
        
#         removed_item = self.queue[self.front]
#         self.queue[self.front] = None
        
#         if self.front == self.rear:
#             self.front = -1
#             self.rear = -1
#         else:
#             self.front = (self.front + 1) % self.capacity
        
#         self.display(f"setelah nilai {removed_item} keluar")
#         return removed_item
    
#     def display(self, message):
#         print(f"{message}  --> {self.queue}")

# # Uji dengan input pertama dan kedua
# queue1 = CircularQueue(5)
# queue2 = CircularQueue(7)

# print("\n================Circular Queue ukuran 5==================")
# for num in [1, 2, 3, 4, 5]:
#     queue1.enqueue(num)
# queue1.enqueue(6)  # Uji kondisi penuh
# queue1.dequeue()
# queue1.dequeue()
# queue1.enqueue(6)
# queue1.enqueue(7)

# print("\n================Circular Queue ukuran 7==================")
# for num in [10, 20, 30, 40, 50, 60, 70]:
#     queue2.enqueue(num)
# queue2.enqueue(80)  # Uji kondisi penuh
# queue2.dequeue()
# queue2.dequeue()
# queue2.enqueue(80)
# queue2.enqueue(90)





#2C deque (doubel ended queue)
# from collections import deque

# class Deque:
#     def __init__(self):
#         self.deque = deque()

#     def add_front(self, item):
#         self.deque.appendleft(item)
#         self.display(f"setelah nilai {item} ditambahkan di depan")

#     def add_rear(self, item):
#         self.deque.append(item)
#         self.display(f"setelah nilai {item} ditambahkan di belakang")

#     def remove_front(self):
#         if not self.deque:
#             print("Deque kosong! Tidak bisa remove dari depan")
#             return None
#         removed_item = self.deque.popleft()
#         self.display(f"setelah nilai {removed_item} dihapus dari depan")
#         return removed_item

#     def remove_rear(self):
#         if not self.deque:
#             print("Deque kosong! Tidak bisa remove dari belakang")
#             return None
#         removed_item = self.deque.pop()
#         self.display(f"setelah nilai {removed_item} dihapus dari belakang")
#         return removed_item

#     def display(self, message):
#         print(f"{message}  --> {list(self.deque)}")

# # Uji dengan input pertama dan kedua
# deque1 = Deque()
# deque2 = Deque()

# print("\n================Deque #1==================")
# for num in [100, 200, 300]:
#     deque1.add_front(num)
# for num in [400, 500]:
#     deque1.add_rear(num)
# deque1.remove_front()
# deque1.remove_rear()

# print("\n================Deque #2==================")
# for num in [10, 20, 30]:
#     deque2.add_rear(num)
# for num in [40, 50]:
#     deque2.add_front(num)
# deque2.remove_front()
# deque2.remove_rear()





#2D priorty queue
# import heapq

# class PriorityQueue:
#     def __init__(self):
#         self.queue = []

#     def enqueue(self, priority, item):
#         heapq.heappush(self.queue, (priority, item))
#         self.display(f"setelah nilai ({priority}, {item}) ditambahkan")

#     def dequeue(self):
#         if not self.queue:
#             print("Priority Queue kosong! Tidak bisa dequeue")
#             return None
#         removed_item = heapq.heappop(self.queue)
#         self.display(f"setelah nilai {removed_item} diproses")
#         return removed_item

#     def display(self, message):
#         print(f"{message}  --> {self.queue}")

# # Uji dengan input pertama dan kedua
# pq1 = PriorityQueue()
# pq2 = PriorityQueue()

# print("\n================Priority Queue #1==================")
# for item in [(2, 100), (1, 200), (3, 50)]:
#     pq1.enqueue(*item)
# pq1.dequeue()
# pq1.dequeue()
# pq1.dequeue()

# print("\n================Priority Queue #2==================")
# for item in [(5, 10), (3, 30), (4, 20)]:
#     pq2.enqueue(*item)
# pq2.dequeue()
# pq2.dequeue()
# pq2.dequeue()





#2E queue dengan double linked list
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class QueueLinkedList:
#     def __init__(self):
#         self.front = None
#         self.rear = None

#     def is_empty(self):
#         return self.front is None

#     def enqueue(self, data):
#         new_node = Node(data)
#         if self.rear is None:
#             self.front = self.rear = new_node
#         else:
#             self.rear.next = new_node
#             self.rear = new_node
#         self.display(f"setelah nilai {data} masuk")

#     def dequeue(self):
#         if self.is_empty():
#             print("Queue kosong! Tidak bisa dequeue")
#             return None
#         removed_data = self.front.data
#         self.front = self.front.next
#         if self.front is None:
#             self.rear = None
#         self.display(f"setelah nilai {removed_data} keluar")
#         return removed_data

#     def display(self, message):
#         current = self.front
#         elements = []
#         while current:
#             elements.append(current.data)
#             current = current.next
#         print(f"{message}  --> {elements}")

# # Uji dengan input pertama dan kedua
# queue1 = QueueLinkedList()
# queue2 = QueueLinkedList()

# print("\n================Queue dengan Linked List #1==================")
# for num in [8, 16, 24, 32, 40]:
#     queue1.enqueue(num)
# queue1.dequeue()
# queue1.dequeue()

# print("\n================Queue dengan Linked List #2==================")
# for num in [11, 22, 33, 44, 55]:
#     queue2.enqueue(num)
# queue2.dequeue()
# queue2.dequeue()
