import tkinter as tk
from tkinter import messagebox

def is_valid_move(board, row, col, n):
    """Kiểm tra xem có thể đặt quân mã tại (row, col) không."""
    moves = [
        (-2, -1), (-1, -2), (1, -2), (2, -1),
        (2, 1), (1, 2), (-1, 2), (-2, 1)
    ]
    for dr, dc in moves:
        r, c = row + dr, col + dc
        if 0 <= r < n and 0 <= c < n and board[r][c] == 1:
            return False
    return True


def greedy_knight_placement(n):
    """Đặt tối đa quân mã trên bàn cờ n x n bằng thuật toán tham lam."""
    board = [[0] * n for _ in range(n)]  # Khởi tạo bàn cờ với giá trị 0
    max_knights = (n * n + 1) // 2  # Số quân mã tối đa
    placed_knights = 0  # Số quân mã đã đặt

    for row in range(n):
        for col in range(n):
            if (row + col) % 2 == 0:  # Tham lam đặt trên ô trắng trước (ô đen cũng hợp lệ)
                if is_valid_move(board, row, col, n):
                    board[row][col] = 1  # Đặt quân mã
                    placed_knights += 1
                    if placed_knights == max_knights:
                        return board, placed_knights

    return board, placed_knights

def draw_board(board, n, placed_knights):
    """Vẽ bàn cờ lên giao diện GUI với ký hiệu quân mã '♞' và hiển thị số quân mã đã xếp."""
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
    knights_label = tk.Label(window, text=f"Số quân mã đã xếp: {placed_knights}", font=("Arial", 14))
    knights_label.grid(row=n, column=0, columnspan=n, pady=10)

    window.mainloop()

def on_submit():
    """Xử lý sự kiện khi người dùng nhập số n và nhấn nút Submit."""
    try:
        n = int(entry.get())  # Lấy giá trị từ ô nhập liệu
        if n <= 0:
            raise ValueError
        board, placed_knights = greedy_knight_placement(n)
        draw_board(board, n, placed_knights)
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
