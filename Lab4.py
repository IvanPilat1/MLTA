import tkinter as tk
from tkinter import ttk, messagebox


# ---------- Кількість шляхів ----------
def print_matrix(dp):
    text = ""
    for row in dp:
        text += "  ".join(f"{val:3}" for val in row) + "\n"
    text += "\n" + "-" * 40 + "\n"
    return text


def count_paths(x, y, output):
    try:
        x = int(x)
        y = int(y)
        if x < 0 or y < 0:
            raise ValueError

        dp = [[0] * (y + 1) for _ in range(x + 1)]
        result_text = "Початкова матриця:\n" + print_matrix(dp)

        for i in range(x + 1):
            dp[i][0] = 1
        result_text += "Після заповнення першого стовпця:\n" + print_matrix(dp)

        for j in range(y + 1):
            dp[0][j] = 1
        result_text += "Після заповнення першого рядка:\n" + print_matrix(dp)

        for i in range(1, x + 1):
            for j in range(1, y + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        result_text += "Кінцева таблиця DP:\n" + print_matrix(dp)
        result_text += f"Кількість шляхів від (0,0) до ({x},{y}): {dp[x][y]}"

        output.delete(1.0, tk.END)
        output.insert(tk.END, result_text)

    except ValueError:
        messagebox.showerror("Помилка", "Введіть цілі додатні числа для x і y!")


# ---------- Мінімальна кількість купюр ----------
def min_banknotes(n, output):
    try:
        n = int(n)
        if n <= 0:
            raise ValueError

        denominations = [500, 200, 100, 50, 20, 10, 5, 2, 1]
        result = {}
        total_bills = 0

        for d in denominations:
            if n >= d:
                count = n // d
                n = n % d
                result[d] = count
                total_bills += count

        text = "Мінімальна кількість купюр:\n\n"
        for denom, count in result.items():
            text += f"{denom} грн — {count} шт.\n"
        text += f"\nЗагальна кількість купюр: {total_bills}"

        output.delete(1.0, tk.END)
        output.insert(tk.END, text)

    except ValueError:
        messagebox.showerror("Помилка", "Введіть додатну суму у гривнях!")


# ---------- Головне вікно ----------
root = tk.Tk()
root.title("Алгоритмічні задачі")
root.geometry("600x600")

# Створення вкладок
tab_control = ttk.Notebook(root)

# --------- Вкладка 1 ---------
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text="Кількість шляхів")

tk.Label(tab1, text="Введіть x:").pack(pady=5)
entry_x = tk.Entry(tab1)
entry_x.pack()

tk.Label(tab1, text="Введіть y:").pack(pady=5)
entry_y = tk.Entry(tab1)
entry_y.pack()

btn1 = tk.Button(tab1, text="Обчислити шляхи", command=lambda: count_paths(entry_x.get(), entry_y.get(), output1))
btn1.pack(pady=10)

output1 = tk.Text(tab1, height=25, width=70)
output1.pack()

# --------- Вкладка 2 ---------
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text="Мінімальна кількість купюр")

tk.Label(tab2, text="Введіть суму премії (грн):").pack(pady=5)
entry_n = tk.Entry(tab2)
entry_n.pack()

btn2 = tk.Button(tab2, text="Розрахувати купюри", command=lambda: min_banknotes(entry_n.get(), output2))
btn2.pack(pady=10)

output2 = tk.Text(tab2, height=25, width=70)
output2.pack()

# Показуємо вкладки
tab_control.pack(expand=1, fill="both")

root.mainloop()
