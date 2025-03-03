
# a) O(2n) 
n = 5

# Literasi pertama sebanyak n kali
for i in range(1, n + 1):
    print(f"Literasi pertama ke-{i}")

# Literasi kedua sebanyak n kali
for i in range(1, n + 1):
    print(f"Literasi kedua ke-{i}")
    


# b) O(n+n2) 
n = 5

# Perulangan pertama (O(n))
for i in range(1, n + 1):
    print(f"Literasi linear ke-{i}")

# Perulangan kedua (O(n^2))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"Literasi kuadratik ke-{i},{j}")