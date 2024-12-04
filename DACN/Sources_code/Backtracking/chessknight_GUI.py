import tkinter as tk
from tkinter import messagebox

# Hàm kiểm tra xem quân mã tại (row, col) có an toàn không
def is_safe(board, row, col, n):
    knight_moves = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]
    for move in knight_moves:
        new_row, new_col = row + move[0], col + move[1]
        if 0 <= new_row < n and 0 <= new_col < n and board[new_row][new_col] == 1:
            return False
    return True

# Hàm tối ưu số quân mã có thể đặt và lưu vị trí các quân mã
def knights(board, n, current_knights, max_knights, row, col, positions):
    max_knights[0] = max(max_knights[0], current_knights)

    for r in range(row, n):
        for c in range(col, n):
            if board[r][c] == 0 and is_safe(board, r, c, n):
                board[r][c] = 1
                positions.append((r, c))  # Lưu vị trí quân mã
                knights(board, n, current_knights + 1, max_knights, r, c + 1, positions)
                positions.pop()  # Xóa vị trí khi quay lại
                board[r][c] = 0
        col = 0 

    return max_knights[0]

# Hàm xử lý khi nhấn nút "Tính toán"
def solve_knights_gui():
    try:
        n = int(entry_size.get())
        if n <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Lỗi", "Kích thước bàn cờ phải là số nguyên dương!")
        return

    board = [[0 for _ in range(n)] for _ in range(n)]
    max_knights_result = [0]  # Dùng mảng để lưu giá trị tham chiếu
    positions = []  # Danh sách lưu các vị trí quân mã
    result = knights(board, n, 0, max_knights_result, 0, 0, positions)

    result_label.config(text=f"Số quân mã tối đa có thể đặt trên bàn cờ {n}x{n}: {result}")

    # Cập nhật bàn cờ
    update_board_gui(n, positions)

# Hàm cập nhật bàn cờ và hiển thị quân mã
def update_board_gui(n, positions):
    # Xóa nội dung cũ trong Canvas
    canvas.delete("all")

    # Vẽ bàn cờ
    cell_size = 40
    for i in range(n):
        for j in range(n):
            x1, y1 = j * cell_size, i * cell_size
            x2, y2 = x1 + cell_size, y1 + cell_size
            color = "white" if (i + j) % 2 == 0 else "gray"
            canvas.create_rectangle(x1, y1, x2, y2, fill=color)

    # Vẽ quân mã
    for (row, col) in positions:
        x1, y1 = col * cell_size, row * cell_size
        x2, y2 = x1 + cell_size, y1 + cell_size
        canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="♞", font=("Arial", 20, "bold"))

# Giao diện GUI
root = tk.Tk()
root.title("Bài toán Sắp xếp quân mã trên bàn cờ")

# Label và Entry cho kích thước bàn cờ
label_size = tk.Label(root, text="Nhập kích thước bàn cờ (n):")
label_size.pack(pady=5)

entry_size = tk.Entry(root)
entry_size.pack(pady=5)

# Nút tính toán
calculate_button = tk.Button(root, text="Tính toán", command=solve_knights_gui)
calculate_button.pack(pady=10)

# Label kết quả
result_label = tk.Label(root, text="Số quân mã tối đa có thể đặt: ")
result_label.pack(pady=10)

# Canvas để vẽ bàn cờ
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack(pady=20)

# Chạy giao diện
root.mainloop()
