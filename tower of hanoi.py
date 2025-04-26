def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f" pindahkan cakram 1 dari {source} ke {target}")
        return
    tower_of_hanoi(n - 1, source, target, auxiliary)
    print(f"pindahkan cakram {n} dari {source} ke {target}")
    tower_of_hanoi(n - 1, auxiliary, source, target)

n = int(input("masukan cakram"))
tower_of_hanoi(n, 'A', 'B', 'C')
