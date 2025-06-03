import heapq
import itertools
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, name):
        self.vertices[name] = {}

    def add_edge(self, from_vertex, to_vertex, weight):
        self.vertices[from_vertex][to_vertex] = weight
        self.vertices[to_vertex][from_vertex] = weight  # undirected

# Data kota dan jarak
kota = [
    'Jepara', 'Kudus', 'Semarang', 'Salatiga', 'Yogyakarta',
    'Purworejo', 'Kebumen', 'Wonosobo', 'Pekalongan', 'Purwokerto'
]

edges = [
    ('Jepara', 'Kudus', 35), ('Kudus', 'Semarang', 50), ('Semarang', 'Salatiga', 45),
    ('Salatiga', 'Yogyakarta', 80), ('Yogyakarta', 'Purworejo', 30),
    ('Purworejo', 'Kebumen', 35), ('Kebumen', 'Purwokerto', 50),
    ('Purwokerto', 'Pekalongan', 90), ('Pekalongan', 'Wonosobo', 60),
    ('Wonosobo', 'Kebumen', 40), ('Wonosobo', 'Purworejo', 30),
    ('Wonosobo', 'Semarang', 70), ('Pekalongan', 'Jepara', 100),
    ('Kudus', 'Salatiga', 55), ('Kebumen', 'Yogyakarta', 60),
    ('Purwokerto', 'Wonosobo', 75), ('Pekalongan', 'Semarang', 60),
    ('Jepara', 'Semarang', 70), ('Purworejo', 'Salatiga', 50),
    ('Purwokerto', 'Yogyakarta', 85), ('Jepara', 'Salatiga', 90),
    ('Kudus', 'Yogyakarta', 120), ('Semarang', 'Yogyakarta', 100),
    ('Kebumen', 'Salatiga', 65), ('Purworejo', 'Semarang', 75),
    ('Pekalongan', 'Kudus', 80), ('Jepara', 'Purworejo', 110),
    ('Kebumen', 'Semarang', 95), ('Wonosobo', 'Salatiga', 40),
    ('Purwokerto', 'Salatiga', 95), ('Yogyakarta', 'Semarang', 100)
]

# Koordinat kota (longitude, latitude)
koordinat_kota = {
    'Jepara': (110.675, -6.584),
    'Kudus': (110.841, -6.805),
    'Semarang': (110.428, -6.966),
    'Salatiga': (110.508, -7.330),
    'Yogyakarta': (110.369, -7.795),
    'Purworejo': (110.012, -7.713),
    'Kebumen': (109.654, -7.676),
    'Wonosobo': (109.901, -7.358),
    'Pekalongan': (109.675, -6.889),
    'Purwokerto': (109.234, -7.424)
}

# Bangun graph
peta = Graph()
for k in kota:
    peta.add_vertex(k)
for e in edges:
    peta.add_edge(*e)

# Fungsi Dijkstra
def dijkstra(graph, start, end):
    queue = [(0, start, [])]
    visited = set()
    while queue:
        (cost, node, path) = heapq.heappop(queue)
        if node in visited:
            continue
        path = path + [node]
        visited.add(node)
        if node == end:
            return (cost, path)
        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                heapq.heappush(queue, (cost + weight, neighbor, path))
    return (float("inf"), [])

# Fungsi TSP
def tsp_no_return(graph, start):
    vertices = list(graph.keys())
    vertices.remove(start)
    min_path = None
    min_cost = float("inf")
    for perm in itertools.permutations(vertices):
        cost = 0
        k = start
        valid = True
        for j in perm:
            if j in graph[k]:
                cost += graph[k][j]
                k = j
            else:
                valid = False
                break
        if valid and cost < min_cost:
            min_cost = cost
            min_path = (start,) + perm
    return (min_cost, min_path) if min_path else (float("inf"), [])

# Visualisasi dengan Matplotlib
def visualisasi_graph(graph_data):
    G = nx.Graph()
    for kota_asal, tetangga in graph_data.items():
        for kota_tujuan, jarak in tetangga.items():
            if not G.has_edge(kota_asal, kota_tujuan):
                G.add_edge(kota_asal, kota_tujuan, weight=jarak)
    pos = koordinat_kota
    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=1500, font_size=9, font_weight='bold', edge_color='gray')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=7)
    plt.title("Peta Rute Kota Berdasarkan Lokasi Geografis", fontsize=14)
    plt.axis('off')
    plt.show()
                
# ===== INTERAKTIF USER =====
print("\n=== SIMULASI GPS BERBASIS MOBIL (Jawa Tengah) ===")
print("Kota yang tersedia:")
for k in kota:
    print(f"- {k}")

asal = input("\nMasukkan kota asal: ").title()
tujuan = input("Masukkan kota tujuan: ").title()

if asal not in kota or tujuan not in kota:
    print("Kota tidak ditemukan.")
else:
    # Struktur graf
    print("\n=== STRUKTUR GRAPH (Koneksi Antar Kota) ===")
    for kota_asal, tetangga in peta.vertices.items():
        jalur = ", ".join(f"{kota_tujuan} ({jarak} km)" for kota_tujuan, jarak in tetangga.items())
        print(f"{kota_asal} => {jalur}")

    # Dijkstra
    jarak, rute = dijkstra(peta.vertices, asal, tujuan)
    kecepatan = 60
    waktu = round(jarak / kecepatan, 2)
    print(f"\n=== DIJKSTRA ({asal} ke {tujuan}) ===")
    print(f"Jalur tercepat: {' -> '.join(rute)}")
    print(f"Total jarak: {jarak} km, Estimasi waktu: {waktu} jam")

    # TSP
    tsp_jarak, tsp_rute = tsp_no_return(peta.vertices, asal)
    tsp_waktu = round(tsp_jarak / kecepatan, 2)
    print(f"\n=== TSP TANPA KEMBALI KE ASAL ({asal}) ===")
    print(f"Rute terbaik: {' -> '.join(tsp_rute)}")
    print(f"Total jarak: {tsp_jarak} km, Estimasi waktu: {tsp_waktu} jam")


    # Visualisasi
    visualisasi_graph(peta.vertices)
