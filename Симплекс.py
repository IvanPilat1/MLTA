# --- Уніфікований список із 30 симплекс-задач ---

tasks_all = [

    # 🔹 1
    {"name": "Maximize Z = 5x1 + 4x2 + 3x3", "type": "max",
     "c": [5, 4, 3],
     "A": [[2, 1, 1], [1, 3, 2], [2, 1, 3]],
     "b": [8, 12, 10],
     "signs": ["<=", "<=", "<="],
     "bounds": [(0, None), (0, None), (0, None)]},

    # 🔹 2
    {"name": "Minimize Z = 6x1 + 3x2 + 5x3 + 2x4", "type": "min",
     "c": [6, 3, 5, 2],
     "A": [[1, 2, 1, 1], [3, 1, 2, 1], [2, 3, 2, 3]],
     "b": [10, 12, 18],
     "signs": [">=", ">=", ">="],
     "bounds": [(0, None)] * 4},

    # 🔹 3
    {"name": "Maximize Z = 7x1 + 5x2 + 4x3 + 6x4", "type": "max",
     "c": [7, 5, 4, 6],
     "A": [[2, 1, 3, 2], [1, 4, 2, 1], [3, 2, 1, 2]],
     "b": [16, 12, 18],
     "signs": ["<=", "<=", "<="],
     "bounds": [(0, None)] * 4},

    # 🔹 4
    {"name": "Minimize Z = 3x1 + 2x2 + 4x3", "type": "min",
     "c": [3, 2, 4],
     "A": [[1, 2, 3], [2, 1, 1], [1, 0, 1]],
     "b": [8, 6, 3],
     "signs": ["=", "=", "="],
     "bounds": [(0, None)] * 3},

    # 🔹 5
    {"name": "Maximize Z = 4x1 + 3x2 + 2x3 + 5x4 (x1 < 0)", "type": "max",
     "c": [4, 3, 2, 5],
     "A": [[1, 2, 1, 3], [2, 1, 3, 1], [1, 3, 2, 2]],
     "b": [15, 18, 20],
     "signs": ["<=", "<=", "<="],
     "bounds": [(None, 0), (0, None), (0, None), (0, None)]},

    # 🔹 6
    {"name": "Maximize Z = 8x1 - 2x2 + 4x3", "type": "max",
     "c": [8, -2, 4],
     "A": [[2, 1, 1], [1, 3, 2], [1, 1, 4]],
     "b": [14, 18, 20],
     "signs": ["<=", "<=", "<="],
     "bounds": [(0, None)] * 3},

    # 🔹 7
    {"name": "Minimize Z = 5x1 + 3x2 - 4x3 + 2x4", "type": "min",
     "c": [5, 3, -4, 2],
     "A": [[1, 2, 1, 1], [2, 1, 3, 2], [1, 1, 2, 3]],
     "b": [10, 24, 16],
     "signs": [">=", ">=", ">="],
     "bounds": [(0, None)] * 4},

    # 🔹 8
    {"name": "Maximize Z = 7x1 - x2 + 6x3 - 2x4", "type": "max",
     "c": [7, -1, 6, -2],
     "A": [[2, 1, 3, 1], [1, 4, 1, 2], [3, 1, 2, 3]],
     "b": [22, 20, 30],
     "signs": ["<=", "<=", "<="],
     "bounds": [(0, None)] * 4},

    # 🔹 9
    {"name": "Minimize Z = -3x1 + 4x2 + 2x3", "type": "min",
     "c": [-3, 4, 2],
     "A": [[1, 2, 1], [2, 1, 3], [1, 1, 1]],
     "b": [12, 18, 15],
     "signs": ["=", "=", "<="],
     "bounds": [(0, None)] * 3},

    # 🔹 10
    {"name": "Maximize Z = 4x1 + 2x2 - 5x3", "type": "max",
     "c": [4, 2, -5],
     "A": [[1, 3, 2], [2, 1, 1], [1, 1, 4]],
     "b": [25, 20, 30],
     "signs": ["<=", "<=", "<="],
     "bounds": [(0, None)] * 3},

    # 🔹 11
    {"name": "Maximize Z = 9x1 - 3x2 + 5x3", "type": "max",
     "c": [9, -3, 5],
     "A": [[2, 1, 1], [1, 3, 2], [3, 1, 2]],
     "b": [20, 30, 24],
     "signs": ["<=", "<=", "<="],
     "bounds": [(0, None)] * 3},

    # 🔹 12
    {"name": "Minimize Z = 4x1 + 2x2 - 6x3 + x4", "type": "min",
     "c": [4, 2, -6, 1],
     "A": [[1, 2, 1, 1], [2, 1, 3, 2], [1, 1, 2, 3]],
     "b": [14, 28, 18],
     "signs": [">=", ">=", ">="],
     "bounds": [(0, None)] * 4},

    # 🔹 13
    {"name": "Maximize Z = 6x1 + x2 - 2x3 + 4x4", "type": "max",
     "c": [6, 1, -2, 4],
     "A": [[2, 1, 3, 1], [1, 4, 1, 2], [3, 2, 2, 3]],
     "b": [26, 22, 36],
     "signs": ["<=", "<=", "<="],
     "bounds": [(0, None)] * 4},

    # 🔹 14
    {"name": "Minimize Z = -2x1 + 5x2 + 3x3", "type": "min",
     "c": [-2, 5, 3],
     "A": [[1, 2, 1], [2, 1, 3], [1, 1, 2]],
     "b": [10, 20, 18],
     "signs": ["=", "=", "<="],
     "bounds": [(0, None)] * 3},

    # 🔹 15
    {"name": "Maximize Z = 5x1 - 4x2 + 3x3", "type": "max",
     "c": [5, -4, 3],
     "A": [[1, 1, 1], [2, 3, 1], [1, 2, 4]],
     "b": [12, 30, 28],
     "signs": ["<=", "<=", "<="],
     "bounds": [(0, None)] * 3},

    # 🔹 16
    {"name": "Minimize Z = 3x1 + x2 - x3 + 2x4", "type": "min",
     "c": [3, 1, -1, 2],
     "A": [[2, 1, 1, 1], [1, 3, 2, 1], [3, 1, 2, 2]],
     "b": [16, 20, 24],
     "signs": [">=", ">=", ">="],
     "bounds": [(0, None)] * 4},

    # 🔹 17
    {"name": "Maximize Z = 8x1 + 2x2 - 3x3 + x4", "type": "max",
     "c": [8, 2, -3, 1],
     "A": [[3, 1, 1, 2], [1, 4, 2, 1], [2, 2, 3, 3]],
     "b": [34, 28, 40],
     "signs": ["<=", "<=", "<="],
     "bounds": [(0, None)] * 4},

    # 🔹 18
    {"name": "Minimize Z = -x1 + 4x2 + 2x3", "type": "min",
     "c": [-1, 4, 2],
     "A": [[1, 1, 2], [2, 3, 1], [1, 2, 3]],
     "b": [14, 30, 26],
     "signs": ["<=", "<=", "<="],
     "bounds": [(0, None)] * 3},

    # 🔹 19
    {"name": "Maximize Z = 7x1 - 2x2 + 4x3", "type": "max",
     "c": [7, -2, 4],
     "A": [[2, 1, 2], [1, 3, 1], [3, 1, 4]],
     "b": [18, 22, 30],
     "signs": ["<=", "<=", "<="],
     "bounds": [(0, None)] * 3},

    # 🔹 20
    {"name": "Minimize Z = 2x1 - 3x2 + x3 + 5x4", "type": "min",
     "c": [2, -3, 1, 5],
     "A": [[1, 2, 1, 1], [2, 1, 2, 3], [1, 1, 3, 2]],
     "b": [20, 36, 28],
     "signs": [">=", ">=", ">="],
     "bounds": [(0, None)] * 4},

    # 🔹 21–30 (форматовано з tasks_4)
    {"name": "Задача 21", "type": "max",
     "c": [6, -2, 3],
     "A": [[1, 1, 2], [2, 3, 1], [1, 4, 3]],
     "b": [20, 25, 30],
     "signs": ["<=", "<=", "<="],
     "bounds": [(0, None)] * 3},

    {"name": "Задача 22", "type": "min",
     "c": [4, -1, 5, 2],
     "A": [[2, 1, 1, 1], [1, 3, 2, 3], [3, 2, 2, 1]],
     "b": [15, 25, 30],
     "signs": [">=", ">=", ">="],
     "bounds": [(0, None)] * 4},

    {"name": "Задача 23", "type": "max",
     "c": [7, 2, -4, 3],
     "A": [[2, 1, 3, 2], [1, 2, 2, 1], [3, 1, 1, 3]],
     "b": [40, 25, 35],
     "signs": ["<=", "<=", "<="],
     "bounds": [(0, None)] * 4},

    {"name": "Задача 24", "type": "min",
     "c": [-3, 4, 2],
     "A": [[1, 1, 1], [2, 1, 3], [1, 3, 2]],
     "b": [15, 25, 30],
     "signs": ["=", "=", "<="],
     "bounds": [(0, None)] * 3},

    {"name": "Задача 25", "type": "max",
     "c": [5, -2, 4],
     "A": [[2, 1, 1], [1, 3, 2], [1, 1, 4]],
     "b": [18, 22, 28],
     "signs": ["<=", "<=", "<="],
     "bounds": [(0, None)] * 3},

    {"name": "Задача 26", "type": "min",
     "c": [2, 3, -1, 4],
     "A": [[1, 1, 2, 1], [3, 2, 1, 2], [2, 3, 2, 3]],
     "b": [18, 25, 32],
     "signs": [">=", ">=", ">="],
     "bounds": [(0, None)] * 4},

    {"name": "Задача 27", "type": "max",
     "c": [9, -3, 2, -1],
     "A": [[3, 2, 1, 1], [1, 4, 2, 3], [2, 1, 3, 2]],
     "b": [30, 35, 40],
     "signs": ["<=", "<=", "<="],
     "bounds": [(0, None)] * 4},

    {"name": "Задача 28", "type": "min",
     "c": [-1, 5, 3],
     "A": [[1, 2, 1], [2, 1, 3], [1, 3, 2]],
     "b": [16, 26, 24],
     "signs": ["<=", "<=", "<="],
     "bounds": [(0, None)] * 3},

    {"name": "Задача 29", "type": "max",
     "c": [4, 3, -5],
     "A": [[2, 1, 1], [1, 3, 2], [3, 2, 3]],
     "b": [20, 25, 35],
     "signs": ["<=", "<=", "<="],
     "bounds": [(0, None)] * 3},

    {"name": "Задача 30", "type": "min",
     "c": [3, -4, 2, 1],
     "A": [[1, 1, 2, 1], [2, 1, 3, 2], [1, 3, 1, 2]],
     "b": [20, 28, 26],
     "signs": [">=", ">=", ">="],
     "bounds": [(0, None)] * 4}
]

import numpy as np
import pandas as pd

# --- Функція для відображення таблиці у вигляді DataFrame ---
def show_tableau(tableau, basic_vars, non_basic_vars, iteration):
    rows = []
    for i, row in enumerate(tableau[:-1]):
        rows.append([basic_vars[i]] + list(np.round(row, 3)))
    rows.append(["Z"] + list(np.round(tableau[-1], 3)))
    cols = ["Базис"] + [f"x{j+1}" for j in range(len(non_basic_vars))] + ["Дод. змінна", "b"]
    df = pd.DataFrame(rows, columns=cols)
    print(f"\n🔸 Ітерація {iteration}")
    print(df.to_string(index=False))

# --- Симплекс-метод ---
def simplex_method(c, A, b):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    c = np.array(c, dtype=float)

    m, n = A.shape

    # Формування початкової симплекс-таблиці
    tableau = np.zeros((m + 1, n + m + 2))
    tableau[:m, :n] = A
    tableau[:m, n:n+m] = np.eye(m)
    tableau[:m, -1] = b
    tableau[-1, :n] = -c

    basic_vars = [f"x{n+i+1}" for i in range(m)]
    non_basic_vars = [f"x{j+1}" for j in range(n)]

    iteration = 0
    show_tableau(tableau, basic_vars, non_basic_vars, iteration)

    # --- Основний цикл симплекс методу ---
    while np.any(tableau[-1, :-1] < 0):
        iteration += 1

        # Крок 1: Вибір стовпця (вхідної змінної)
        col = np.argmin(tableau[-1, :-1])

        # Крок 2: Вибір рядка (вихідної змінної)
        ratios = []
        for i in range(m):
            if tableau[i, col] > 0:
                ratios.append(tableau[i, -1] / tableau[i, col])
            else:
                ratios.append(np.inf)
        row = np.argmin(ratios)
        if np.all(np.isinf(ratios)):
            raise ValueError("Розв’язок не обмежений!")

        pivot = tableau[row, col]
        tableau[row, :] /= pivot

        # Обнулення стовпця
        for i in range(m + 1):
            if i != row:
                tableau[i, :] -= tableau[i, col] * tableau[row, :]

        basic_vars[row] = non_basic_vars[col]

        show_tableau(tableau, basic_vars, non_basic_vars, iteration)

    # --- Результати ---
    solution = {var: 0 for var in non_basic_vars + basic_vars}
    for i in range(m):
        solution[basic_vars[i]] = tableau[i, -1]

    Z = tableau[-1, -1]
    print("\n✅ Оптимальний розв’язок:")
    for var, val in solution.items():
        if not var.startswith("x") or int(var[1:]) <= n:
            print(f"{var} = {val:.3f}")
    print(f"Z = {Z:.3f}")

# --- Приклад ---
if __name__ == "__main__":
    # Максимізація Z = 5x1 + 4x2 + 3x3
    c = [5, 4, 3]
    A = [
        [2, 1, 1],
        [1, 3, 2],
        [2, 2, 3]
    ]
    b = [20, 30, 60]

    simplex_method(c, A, b)
