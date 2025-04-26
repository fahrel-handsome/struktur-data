def faktorial(n):
    hasil = 1
    for i in range(1, n + 1):
        hasil *= i
    return hasil

print("hasil faktorial dengan iterasi:", faktorial(15))

