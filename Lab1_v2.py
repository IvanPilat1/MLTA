import tkinter as tk
from tkinter import scrolledtext
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# --------- Дані ---------
vertices = ["a", "b", "c", "d", "e", "f", "g"]
ms = [[0, 1, 1, 0, 1, 0, 0],  # a
      [1, 0, 0, 1, 1, 0, 0],  # b
      [1, 0, 0, 0, 0, 1, 1],  # c
      [0, 1, 0, 0, 0, 1, 1],  # d
      [1, 1, 0, 0, 0, 1, 0],  # e
      [0, 0, 1, 1, 1, 0, 1],  # f
      [0, 0, 1, 1, 0, 0, 1]]  # g

# --------- Методи (ті, що в тебе були) ---------
def get_edges(ms, vertices):
    edges = []
    n = len(vertices)
    for i in range(n):
        for j in range(i+1, n):
            if ms[i][j] == 1:
                edges.append((vertices[i], vertices[j]))
    return edges

def get_adj_list(ms, vertices):
    adj_list = {v: [] for v in vertices}
    n = len(vertices)
    for i in range(n):
        for j in range(n):
            if ms[i][j] == 1:
                adj_list[vertices[i]].append(vertices[j])
    return adj_list

def get_inc_matrix(ms, vertices, edges):
    n, m = len(vertices), len(edges)
    inc_matrix = [[0]*m for _ in range(n)]
    for k, (u, v) in enumerate(edges):
        i, j = vertices.index(u), vertices.index(v)
        inc_matrix[i][k] = 1
        inc_matrix[j][k] = 1
    return inc_matrix

def show_graph(edges):
    G = nx.Graph()
    G.add_edges_from(edges)
    plt.figure(figsize=(6, 6))
    nx.draw(G, with_labels=True, node_size=700,
            node_color="lightblue", font_size=12, font_weight="bold")
    plt.show()  # це блокує виконання, тому ми викликаємо його після вставки обходів у вікно

# --------- DFS (повертає список у порядку відвідування) ---------
def dfs(adj_list, start):
    visited = set()
    order = []

    def _dfs(u):
        visited.add(u)
        order.append(u)
        # якщо хочеш детермінований (передбачуваний) порядок, можна сортувати сусідів:
        for v in adj_list.get(u, []):
            if v not in visited:
                _dfs(v)

    _dfs(start)
    return order

# --------- BFS (як і раніше) ---------
def bfs(adj_list, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    order = []

    while queue:
        v = queue.popleft()
        order.append(v)
        for neighbor in adj_list[v]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order

# --------- Інтерфейс та запуск (run_program) ---------
def run_program():
    edges = get_edges(ms, vertices)
    adj_list = get_adj_list(ms, vertices)
    inc_matrix = get_inc_matrix(ms, vertices, edges)

    output.delete("1.0", tk.END)

    output.insert(tk.END, "Матриця суміжності:\n")
    output.insert(tk.END, " ".join(vertices) + "\n\n")   # виправлено: перелік вершин як рядок
    for a in ms:
        output.insert(tk.END, f"{a}\n")

    output.insert(tk.END, "\nСписок ребер:\n")
    for e in edges:
        output.insert(tk.END, f"{e}\n")

    output.insert(tk.END, "\nСписок суміжності:\n")
    for v, neighbors in adj_list.items():
        output.insert(tk.END, f"{v}: {neighbors}\n")

    output.insert(tk.END, "\nМатриця інцидентності:\n")
    output.insert(tk.END, "   " + " ".join([f"e{k+1}" for k in range(len(edges))]) + "\n")
    for i, row in enumerate(inc_matrix):
        output.insert(tk.END, f"{vertices[i]} {row}\n")

    # --- ОБХОДИ: запускаємо ПЕРЕД show_graph(), щоб plt.show() не блокував вивід ---
    start_vertex = "a"
    dfs_result = dfs(adj_list, start_vertex)
    bfs_result = bfs(adj_list, start_vertex)

    output.insert(tk.END, f"\nDFS (з вершини {start_vertex}): {dfs_result}\n")
    output.insert(tk.END, f"BFS (з вершини {start_vertex}): {bfs_result}\n")

    # Показати граф (після вставки тексту)
    show_graph(edges)

# --------- Запуск Tkinter ---------
window = tk.Tk()
window.title("Графи – лабораторна 1")

btn = tk.Button(window, text="Старт", command=run_program, font=("Arial", 12))
btn.pack(pady=10)

output = scrolledtext.ScrolledText(window, width=60, height=20, font=("Consolas", 10))
output.pack()

window.mainloop()
