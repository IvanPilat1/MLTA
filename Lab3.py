import tkinter as tk
from tkinter import ttk, scrolledtext, Button
import matplotlib.pyplot as plt
import networkx as nx
import heapq
from prettytable import PrettyTable

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

# --- Алгоритм Дейкстри (з проміжними кроками) ---
def dijkstra_steps(graph, start):
    steps = []
    distances = {vertex: float('inf') for vertex in graph}
    for u in graph:
        for v in graph[u]:
            if v not in distances:
                distances[v] = float('inf')
    distances[start] = 0
    queue = [(0, start)]

    step_num = 1
    while queue:
        current_dist, current_vertex = heapq.heappop(queue)
        if current_dist > distances[current_vertex]:
            continue

        step_info = f"Крок {step_num}: розглядаємо вершину {current_vertex}\n"
        table = PrettyTable(["Вершина", "Відстань від 'a'"])
        for v in sorted(distances.keys()):
            val = distances[v] if distances[v] != float('inf') else "-"
            table.add_row([v, val])
        step_info += str(table) + "\n\n"
        steps.append(step_info)

        for neighbor, weight in graph.get(current_vertex, {}).items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

        step_num += 1

    return distances, steps

# --- Алгоритм Флойда–Воршелла (з проміжними кроками) ---
def floyd_warshall_steps(graph):
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

    steps = []
    step_num = 1
    for k in vertices:
        for i in vertices:
            for j in vertices:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

        table = PrettyTable([" "] + vertices)
        for i in vertices:
            row = [i] + [dist[i][j] if dist[i][j] != float('inf') else '-' for j in vertices]
            table.add_row(row)
        steps.append(f"Крок {step_num}: враховуємо проміжну вершину {k}\n{table}\n\n")
        step_num += 1

    return dist, steps

# --- граф для відображення ---
pos = {
    'a': (0, 0),
    'b': (1, 1),
    'c': (2, 0.9),
    'd': (1, -0.3),
    'e': (0, -1),
    'f': (2.5, -0.5),
    'h': (1.2, -1.5)
}

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

# --- Запуск алгоритмів ---
dijkstra_result, dijkstra_steps_list = dijkstra_steps(graph, 'a')
floyd_result, floyd_steps_list = floyd_warshall_steps(graph)

# --- Tkinter UI ---
root = tk.Tk()
root.title("Алгоритми Дейкстри та Флойда–Воршелла (покроково)")
root.geometry("900x700")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# --- вкладка 1: Дейкстра ---
frame_dijkstra = ttk.Frame(notebook)
notebook.add(frame_dijkstra, text="Алгоритм Дейкстри")

text_dijkstra = scrolledtext.ScrolledText(frame_dijkstra, width=100, height=35)
text_dijkstra.pack(padx=10, pady=10)

text_dijkstra.insert(tk.END, "📘 Покрокове виконання алгоритму Дейкстри:\n\n")
for step in dijkstra_steps_list:
    text_dijkstra.insert(tk.END, step)
text_dijkstra.insert(tk.END, "\n✅ Остаточні відстані від 'a':\n")
final_table = PrettyTable(["Вершина", "Мінімальна відстань"])
for node, dist in sorted(dijkstra_result.items()):
    final_table.add_row([node, dist])
text_dijkstra.insert(tk.END, str(final_table))

# --- вкладка 2: Флойд–Воршелл ---
frame_floyd = ttk.Frame(notebook)
notebook.add(frame_floyd, text="Алгоритм Флойда–Воршелла")

text_floyd = scrolledtext.ScrolledText(frame_floyd, width=100, height=35)
text_floyd.pack(padx=10, pady=10)

text_floyd.insert(tk.END, "📗 Покрокове виконання алгоритму Флойда–Воршелла:\n\n")
for step in floyd_steps_list:
    text_floyd.insert(tk.END, step)

# --- кнопка для графа ---
btn_show_graph = Button(root, text="Показати граф", command=show_graph)
btn_show_graph.pack(pady=10)

root.mainloop()
