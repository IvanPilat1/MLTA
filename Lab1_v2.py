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

vertices_2 = ["a", "b", "c", "d", "e", "f", "h"]
ms_2 = [
    [1, 1, 0, 0, 1, 0, 0],  # a 
    [0, 0, 1, 1, 0, 0, 0],  # b 
    [0, 1, 1, 0, 0, 1, 0],  # c 
    [0, 0, 0, 0, 0, 0, 1],  # d 
    [0, 0, 0, 0, 0, 0, 1],  # e 
    [0, 0, 0, 0, 0, 0, 1],  # f 
    [0, 0, 0, 0, 0, 0, 0]   # h 
]


def get_edges(ms, vertices, directed=False, allow_loops=False):
    edges = []
    n = len(vertices)
    for i in range(n):
        for j in range(n):
            if ms[i][j] == 1:
                if i == j and not allow_loops:
                    continue  
                if not directed and j < i:
                    continue  # щоб не дублювати ребра у ненаправленому графі
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

def show_graph(edges, directed=False):
    G = nx.DiGraph() if directed else nx.Graph()
    G.add_edges_from(edges)
    plt.figure(figsize=(6, 6))
    nx.draw_networkx(G, with_labels=True, node_size=700,
                     node_color="lightblue", font_size=12, font_weight="bold",
                     arrows=directed, arrowstyle="->", arrowsize=15)
    plt.show()

# --------- DFS ---------
def dfs(adj_list, start):
    visited = set()
    order = []
    def _dfs(u):
        visited.add(u)
        order.append(u)
        for v in adj_list.get(u, []):
            if v not in visited:
                _dfs(v)
    _dfs(start)
    return order

# --------- BFS ---------
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

# --------- Функція виконання ---------
def run_program(ms_input, vertices_input, directed=False, allow_loops=False):
    edges = get_edges(ms_input, vertices_input, directed=directed, allow_loops=allow_loops)
    adj_list = get_adj_list(ms_input, vertices_input)
    inc_matrix = get_inc_matrix(ms_input, vertices_input, edges)

    output.delete("1.0", tk.END)

    output.insert(tk.END, "Матриця суміжності:\n")
    output.insert(tk.END, " ".join(vertices_input) + "\n\n")
    for a in ms_input:
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
        output.insert(tk.END, f"{vertices_input[i]} {row}\n")

    start_vertex = vertices_input[0]
    dfs_result = dfs(adj_list, start_vertex)
    bfs_result = bfs(adj_list, start_vertex)

    output.insert(tk.END, f"\nDFS (з вершини {start_vertex}): {dfs_result}\n")
    output.insert(tk.END, f"BFS (з вершини {start_vertex}): {bfs_result}\n")

    show_graph(edges, directed=directed)

# --------- Інтерфейс ---------
window = tk.Tk()
window.title("Графи – лабораторна 1 та 2")

frame = tk.Frame(window)
frame.pack(pady=10)

btn1 = tk.Button(frame, text="Граф 1", 
                 command=lambda: run_program(ms, vertices, directed=False, allow_loops=False),
                 font=("Arial", 12))
btn1.grid(row=0, column=0, padx=10)

btn2 = tk.Button(frame, text="Граф 2", 
                 command=lambda: run_program(ms_2, vertices_2, directed=True, allow_loops=True),
                 font=("Arial", 12))
btn2.grid(row=0, column=1, padx=10)

output = scrolledtext.ScrolledText(window, width=60, height=20, font=("Consolas", 10))
output.pack()

window.mainloop()
