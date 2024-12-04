import tkinter as tk
from tkinter import messagebox

# Tạo bàn cờ với các ô đen trắng xen kẽ
def create_board(n):

    global cells, board_frame
    for widget in board_frame.winfo_children():
        widget.destroy()
    
    cells = [[None] * n for _ in range(n)]
    cell_size = 400 // n
    for i in range(n):
        for j in range(n):
            color = "white" if (i + j) % 2 == 0 else "black"
            cell = tk.Label(board_frame, bg=color, width=2, height=1)
            cell.grid(row=i, column=j, padx=1, pady=1, ipadx=cell_size // 2, ipady=cell_size // 6)
            cells[i][j] = cell

def place_knights(n):
    create_board(n)
    knights = []
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:  # Đặt mã trên các ô đen (hoặc ô trắng)
                knights.append((i, j))
                cells[i][j].config(text="♞", fg="red")
    messagebox.showinfo("Kết quả", f"Số lượng mã tối đa: {len(knights)}")

def on_start():
    try:
        n = int(size_entry.get())
        if n < 1:
            raise ValueError
        place_knights(n)
    except ValueError:
        messagebox.showerror("Lỗi", "Hãy nhập một số nguyên dương!")

# Tạo giao diện chính
root = tk.Tk()
root.title("Bàn cờ Mã không khống chế")
root.geometry("500x500")

# Frame nhập kích thước và nút bắt đầu
control_frame = tk.Frame(root)
control_frame.pack(pady=10)

tk.Label(control_frame, text="Kích thước bàn cờ (n):").pack(side=tk.LEFT, padx=5)
size_entry = tk.Entry(control_frame, width=5)
size_entry.pack(side=tk.LEFT, padx=5)
tk.Button(control_frame, text="Bắt đầu", command=on_start).pack(side=tk.LEFT, padx=5)

# Frame để hiển thị bàn cờ
board_frame = tk.Frame(root)
board_frame.pack(pady=10)

# Chạy chương trình
root.mainloop()
