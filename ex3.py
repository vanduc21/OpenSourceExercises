import numpy as np
import tkinter as tk
from tkinter import messagebox





def solve():
    try:
        n = int(entry_n.get())
        A = []
        for i in range(n):
            row = list(map(float, entries_A[i].get().split()))
            A.append(row)
        A = np.array(A)

        b = list(map(float, entry_b.get().split()))
        b = np.array(b)
        A1= np.linalg.inv(A)
        # Giải hệ phương trình
        x = np.dot(A1,b)

        if x is not None:
            messagebox.showinfo("Kết quả", f"Nghiệm của hệ là: {x}")
    except ValueError:
        messagebox.showerror("Error", "Vui lòng nhập đúng định dạng số.")


def create_entries():
    try:
        n = int(entry_n.get())
        for widget in frame_matrix.winfo_children():
            widget.destroy()  # Xóa các ô nhập liệu cũ

        global entries_A
        entries_A = []

        # Tạo các ô nhập liệu cho ma trận A
        for i in range(n):
            label = tk.Label(frame_matrix, text=f"Dòng {i + 1}:")
            label.pack()
            entry = tk.Entry(frame_matrix, width=40)
            entry.pack(padx=5, pady=5)
            entries_A.append(entry)

        label_b = tk.Label(frame_matrix, text="Nhập vectơ b:")
        label_b.pack()

        global entry_b
        entry_b = tk.Entry(frame_matrix, width=40)
        entry_b.pack(padx=5, pady=5)
    except ValueError:
        messagebox.showerror("Error", "Vui lòng nhập số nguyên hợp lệ.")


# Tạo cửa sổ chính
root = tk.Tk()
root.title("Giải hệ phương trình tuyến tính")

# Nhập số lượng phương trình
frame_input = tk.Frame(root)
frame_input.pack(pady=10)

label_n = tk.Label(frame_input, text="Số lượng phương trình (n):")
label_n.pack(side=tk.LEFT, padx=5)

entry_n = tk.Entry(frame_input, width=5)
entry_n.pack(side=tk.LEFT, padx=5)

button_create = tk.Button(frame_input, text="Tạo ma trận", command=create_entries)
button_create.pack(side=tk.LEFT, padx=10)

# Khung để nhập ma trận và vectơ b
frame_matrix = tk.Frame(root)
frame_matrix.pack(pady=10)

# Nút để giải hệ phương trình
button_solve = tk.Button(root, text="Giải hệ phương trình", command=solve)
button_solve.pack(pady=20)

root.mainloop()