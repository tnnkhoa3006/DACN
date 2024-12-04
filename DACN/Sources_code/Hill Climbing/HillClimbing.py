import random

def is_safe(board, x, y, n):
    # Kiểm tra xem mã tại (x, y) có bị mã khác khống chế không
    moves = [(2, 1), (1, 2), (-2, 1), (-1, 2), (2, -1), (1, -2), (-2, -1), (-1, -2)]
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 1:
            return False
    return True

def hill_climbing(n):
    # Khởi tạo bàn cờ trống
    board = [[0] * n for _ in range(n)]
    knights = []  # Danh sách vị trí của các con mã
    max_knights = 0
    
    for _ in range(100):  # Giới hạn số lần khởi động lại
        # Khởi tạo ngẫu nhiên
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

# Kích thước bàn cờ
n = int(input("nhập số ô cho bàn cờ nxn: "))
max_knights, board = hill_climbing(n)
print("Số lượng mã tối đa:", max_knights)
for row in board:
    print(" ".join(str(cell) for cell in row))
