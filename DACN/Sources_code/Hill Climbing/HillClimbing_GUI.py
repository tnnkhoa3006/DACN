import tkinter as tk
from tkinter import messagebox
import random

def is_safe(board, x, y, n):
    """Kiểm tra xem mã tại (x, y) có bị mã khác khống chế không"""
    moves = [(2, 1), (1, 2), (-2, 1), (-1, 2), (2, -1), (1, -2), (-2, -1), (-1, -2)]
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 1:
            return False
    return True

def hill_climbing(n):
    """Sử dụng thuật toán hill climbing để tìm số lượng quân mã tối đa"""
    board = [[0] * n for _ in range(n)]  # Khởi tạo bàn cờ trống
    knights = []  # Danh sách vị trí của các con mã
    max_knights = 0

    for _ in range(100):  # Giới hạn số lần khởi động lại
        board = [[0] * n for _ in range(n)]
        knights = []

        while True:
            # Tìm ô hợp lệ để thêm mã
            candidates = [(x, y) for x in range(n) for y in range(n) if board[x][y] == 0 and is_safe(board, x, y, n)]
            if not candidates:
                break
            x, y = random.choice(candidates)
            board[x][y] = 1
            knights.append((x, y))

        # Cập nhật kết quả tối ưu
        if len(knights) > max_knights:
            max_knights = len(knights)
            best_board = [row[:] for row in board]

    return max_knights, best_board

def draw_board(board, n, max_knights):
    """Vẽ bàn cờ lên giao diện GUI và hiển thị số quân mã tối đa"""
    window = tk.Tk()
    window.title(f"Bàn cờ {n}x{n}")

    # Kích thước mỗi ô vuông trên bàn cờ
    cell_size = 50

    # Vẽ bàn cờ
    for row in range(n):
        for col in range(n):
            color = "white" if (row + col) % 2 == 0 else "black"
            text = "♞" if board[row][col] == 1 else ""  # Hiển thị '♞' nếu có quân mã

            # Tạo label cho mỗi ô và hiển thị ký hiệu quân mã hoặc để trống
            cell = tk.Label(window, width=4, height=2, bg=color, text=text, font=("Arial", 20))
            cell.grid(row=row, column=col)

    # Hiển thị số quân mã đã xếp
    knights_label = tk.Label(window, text=f"Số quân mã tối đa: {max_knights}", font=("Arial", 14))
    knights_label.grid(row=n, column=0, columnspan=n, pady=10)

    window.mainloop()

def on_submit():
    """Xử lý sự kiện khi người dùng nhập số n và nhấn nút Submit"""
    try:
        n = int(entry.get())  # Lấy giá trị từ ô nhập liệu
        if n <= 0:
            raise ValueError
        max_knights, board = hill_climbing(n)
        draw_board(board, n, max_knights)
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập một số nguyên dương.")

# Tạo cửa sổ GUI
root = tk.Tk()
root.title("Bàn cờ Quân Mã")

# Label và Entry để nhập n
label = tk.Label(root, text="Nhập kích thước bàn cờ (n):", font=("Arial", 14))
label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

# Nút Submit để gửi giá trị nhập
submit_button = tk.Button(root, text="Submit", font=("Arial", 14), command=on_submit)
submit_button.pack(pady=10)

# Hiển thị giao diện
root.mainloop()
