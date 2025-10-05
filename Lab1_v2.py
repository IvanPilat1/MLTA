import tkinter as tk
from tkinter import scrolledtext
import networkx as nx
import matplotlib.pyplot as plt


# --------- Дані ---------
vertices = ["a", "b", "c", "d", "e", "f", "g"]
ms = [[0, 1, 1, 0, 1, 0, 0],  # a
      [1, 0, 0, 1, 1, 0, 0],  # b
      [1, 0, 0, 0, 0, 1, 1],  # c
      [0, 1, 0, 0, 0, 1, 1],  # d
      [1, 1, 0, 0, 0, 1, 0],  # e
      [0, 0, 1, 1, 1, 0, 1],  # f
      [0, 0, 1, 1, 0, 0, 1]]  # g


# --------- Методи ---------
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
    plt.show()

def edges_from_inc_matrix(inc_matrix, vertices):
    
    edges = []
    n = len(vertices)      # кількість вершин
    m = len(inc_matrix[0]) # кількість ребер (стовпців)

    for k in range(m):  # ідемо по стовпцях (ребрах)
        connected_vertices = []
        for i in range(n):  # ідемо по вершинах
            if inc_matrix[i][k] == 1:
                connected_vertices.append(vertices[i])
        if len(connected_vertices) == 2:  # ребро з двох вершин
            edges.append((connected_vertices[0], connected_vertices[1]))
    return edges


def adj_matrix_from_inc_matrix(inc_matrix, vertices):
    """
    Побудова матриці суміжності з матриці інцидентності.
    """
    n = len(vertices)
    m = len(inc_matrix[0])
    adj_matrix = [[0]*n for _ in range(n)]

    for k in range(m):  # для кожного ребра
        connected_vertices = []
        for i in range(n):
            if inc_matrix[i][k] == 1:
                connected_vertices.append(i)
        if len(connected_vertices) == 2:
            u, v = connected_vertices
            adj_matrix[u][v] = 1
            adj_matrix[v][u] = 1
    return adj_matrix


def adj_list_from_inc_matrix(inc_matrix, vertices):
    """
    Побудова списку суміжності з матриці інцидентності.
    """
    n = len(vertices)
    m = len(inc_matrix[0])
    adj_list = {v: [] for v in vertices}

    for k in range(m):  # для кожного ребра
        connected_vertices = []
        for i in range(n):
            if inc_matrix[i][k] == 1:
                connected_vertices.append(vertices[i])
        if len(connected_vertices) == 2:
            u, v = connected_vertices
            adj_list[u].append(v)
            adj_list[v].append(u)
    return adj_list

# --------- Інтерфейс ---------
def run_program():
    edges = get_edges(ms, vertices)
    adj_list = get_adj_list(ms, vertices)
    inc_matrix = get_inc_matrix(ms, vertices, edges)

    output.delete("1.0", tk.END)

    output.insert(tk.END, "Матриця суміжності:\n")
    output.insert(tk.END,vertices,"\n")
    output.insert(tk.END,"\n")
    for a in ms:
        output.insert(tk.END, f"{a}\n")

    output.insert(tk.END, "Список ребер:\n")
    for e in edges:
        output.insert(tk.END, f"{e}\n")

    output.insert(tk.END, "\nСписок суміжності:\n")
    for v, neighbors in adj_list.items():
        output.insert(tk.END, f"{v}: {neighbors}\n")

    output.insert(tk.END, "\nМатриця інцидентності:\n")
    output.insert(tk.END, "   " + " ".join([f"e{k+1}" for k in range(len(edges))]) + "\n")
    for i, row in enumerate(inc_matrix):
        output.insert(tk.END, f"{vertices[i]} {row}\n")

    # Показати граф окремим вікном
    show_graph(edges)


# --------- Запуск Tkinter ---------
window = tk.Tk()
window.title("Графи – лабораторна 1")

btn = tk.Button(window, text="Старт", command=run_program, font=("Arial", 12))
btn.pack(pady=10)

output = scrolledtext.ScrolledText(window, width=60, height=20, font=("Consolas", 10))
output.pack()

window.mainloop()
