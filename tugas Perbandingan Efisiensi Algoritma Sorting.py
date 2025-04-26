import time
import random
import matplotlib.pyplot as plt

# Algoritma Sorting
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

def measure_time(sort_func, data):
    data_copy = data.copy()
    start = time.time()
    if sort_func == quick_sort:
        sort_func(data_copy)  # quick_sort returns a new list
    else:
        sort_func(data_copy)  # in-place
    end = time.time()
    return end - start

# Ukuran data dan algoritma
sizes = [100, 500, 1000, 2000]
algorithms = {
    'Bubble Sort': bubble_sort,
    'Insertion Sort': insertion_sort,
    'Selection Sort': selection_sort,
    'Merge Sort': merge_sort,
    'Quick Sort': quick_sort,
}

results = {name: [] for name in algorithms}

for size in sizes:
    test_data = [random.randint(1, 10000) for _ in range(size)]
    for name, func in algorithms.items():
        t = measure_time(func, test_data)
        results[name].append(t)

for name, times in results.items():
    plt.plot(sizes, times, marker='o', label=name)

plt.title("Perbandingan Efisiensi Algoritma Sorting")
plt.xlabel("Ukuran Data")
plt.ylabel("Waktu Eksekusi (detik)")
plt.legend()
plt.grid(True)
plt.show()
