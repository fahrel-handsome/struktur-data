def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

data = [115, 18, 45, 29, 56, 1, 37]
selection_sort(data)
print("Hasil pengurutan:", data)