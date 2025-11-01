import tkinter as tk
from tkinter import scrolledtext, Button
import matplotlib.pyplot as plt
import networkx as nx
import heapq

# --- створення графа ---
edges = [
    ('a', 'b', 2),
    ('a', 'd', 7),
    ('a', 'e', 6),
    ('b', 'c', 6),
    ('b', 'd', 3),
    ('c', 'f', 11),
    ('d', 'h', 4),
    ('e', 'h', 3),
    ('f', 'h', 1)
]

# перетворення в словник
graph = {}
for u, v, w in edges:
    if u not in graph:
        graph[u] = {}
    graph[u][v] = w
print(graph)

# алгоритм Дейкстри 
def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    for u in graph:
        for v in graph[u]:
            if v not in distances:
                distances[v] = float('inf')
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_dist, current_vertex = heapq.heappop(queue)
        if current_dist > distances[current_vertex]:
            continue

        for neighbor, weight in graph.get(current_vertex, {}).items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    return distances

# алгоритм Флойда–Воршелла
def floyd_warshall(graph):
    vertices = set(graph.keys())
    for u in graph:
        for v in graph[u]:
            vertices.add(v)
    vertices = sorted(list(vertices))

    
    dist = {u: {v: float('inf') for v in vertices} for u in vertices}
    for u in vertices:
        dist[u][u] = 0
    for u in graph:
        for v in graph[u]:
            dist[u][v] = graph[u][v]

    
    for k in vertices:
        for i in vertices:
            for j in vertices:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


pos = {
    'a': (0, 0),
    'b': (1, 1),
    'c': (2, 0.9),
    'd': (1, -0.3),
    'e': (0, -1),
    'f': (2.5, -0.5),
    'h': (1.2, -1.5)
}

# --- функція для відображення графа ---
def show_graph():
    G = nx.DiGraph()
    for u, v, w in edges:
        G.add_edge(u, v, weight=w)

    plt.figure(figsize=(7, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1200,
            font_size=12, arrows=True, arrowstyle='-|>', arrowsize=15)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
    plt.title("Граф із вагами ребер", fontsize=14)
    plt.axis('off')
    plt.show()

# --- виконання алгоритмів ---
dijkstra_result = dijkstra(graph, 'a')
floyd_result = floyd_warshall(graph)

# --- інтерфейс Tkinter ---
root = tk.Tk()
root.title("Алгоритми Дейкстри та Флойда–Воршелла")

text_area = scrolledtext.ScrolledText(root, width=80, height=25)
text_area.pack(padx=10, pady=10)

text_area.insert(tk.END, "Найкоротші шляхи від вершини 'a' (алгоритм Дейкстри):\n")
for node, dist in dijkstra_result.items():
    text_area.insert(tk.END, f"a → {node}: {dist}\n")

text_area.insert(tk.END, "\nНайкоротші відстані між усіма парами вершин (алгоритм Флойда–Воршелла):\n")
for u in floyd_result:
    for v in floyd_result[u]:
        dist = floyd_result[u][v]
        if dist == float('inf'):
            text_area.insert(tk.END, f"{u} → {v}: -\n")
        else:
            text_area.insert(tk.END, f"{u} → {v}: {dist}\n")
    text_area.insert(tk.END, "\n")

# --- кнопка ---
btn_show_graph = Button(root, text="Показати граф", command=show_graph)
btn_show_graph.pack(pady=10)

root.mainloop()
