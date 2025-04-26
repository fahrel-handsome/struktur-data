class shorting:
    def __init__(self, arr):
        self.arr = arr
        
    def bubble_sort(self):
        n = len(self.arr)
        for i in range(n):
            swapped = False
            for j in range(n - i - 1):
                if self.arr[j] > self.arr[j + 1]:
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]
                    swapped = True
            if not swapped:
                break
        return self.arr
            
    def bubble_sort_desc(self):
        n = len(self.arr)
        for i in range(n):
            swapped = False
            for j in range(n - i - 1):
                if self.arr[j] < self.arr[j + 1]:
                    self.arr[j], self.arr[j + 1] = self.arr[j+ 1], self.arr[j]
                    swapped = True
            if not swapped:
                break
        return self.arr
            
    def insertion_sort(self):
        for i in range(1, len(self.arr)):
            key = self.arr[i]
            j = i - 1
            while j >= 0 and key < self.arr[j]:
                self.arr[j + 1] = self.arr[j]
                j -= 1
            self.arr[j + 1] = key
        return self.arr
    
    def insertion_sort_desc(self):
        for i in range(1, len(self.arr)):
            key = self.arr[i]
            j = i - 1
            while j >= 0 and key > self.arr[j]:
                self.arr[j + 1] = self.arr[j]
                j -= 1
            self.arr[j + 1] = key
        return self.arr
    
    def selection_sort(self):
        n = len(self.arr)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):   
                if self.arr[j] < self.arr[min_index]:
                    min_index = j
            self.arr[i], self.arr[min_index] = self.arr[min_index], self.arr[i]
            
        return self.arr
    
    def selection_sort_desc(self):
        n = len(self.arr)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if self.arr[j] > self.arr[min_index]:
                    min_index = j
            self.arr[i], self.arr[min_index] = self.arr[min_index], self.arr[i]
                
        return self.arr
        
data = [115, 18, 45, 29, 56, 1, 37]
bubble_sort = shorting(data.copy()). bubble_sort()
insertion_sort = shorting(data.copy()).insertion_sort()
selection_sort = shorting(data.copy()).selection_sort()
print("\ndata setelah diurutkan dengan bubble_sort:", bubble_sort)
print("data setelah diurutkan dengan insertion_sort:", insertion_sort)
print("data setelah diurutkan dengan selection_sort:", selection_sort)

bubble_sort_desc = shorting(data.copy()). bubble_sort_desc()
insertion_sort_desc = shorting(data.copy()).insertion_sort_desc()
selection_sort_desc = shorting(data.copy()).selection_sort_desc()
print("\ndata setelah dibalik dengan bubble_sort:", bubble_sort_desc)
print("data setelah dibalik dengan insertion_sort:", insertion_sort_desc)
print("data setelah dibalik dengan selection_sort:", selection_sort_desc)
                                

            
        