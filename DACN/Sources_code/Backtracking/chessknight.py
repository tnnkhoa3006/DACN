# Hàm kiểm tra xem quân mã tại (row, col) có an toàn không
def is_safe(board, row, col, n):
    knight_moves = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]
    for move in knight_moves:
        new_row, new_col = row + move[0], col + move[1]
        if 0 <= new_row < n and 0 <= new_col < n and board[new_row][new_col] == 1:
            return False
    return True

# Hàm tối ưu số quân mã có thể đặt
def knights(board, n, current_knights, max_knights, row, col):
    max_knights[0] = max(max_knights[0], current_knights)

    for r in range(row, n):
        for c in range(col, n):
            if board[r][c] == 0 and is_safe(board, r, c, n):
                board[r][c] = 1
                knights(board, n, current_knights + 1, max_knights, r, c + 1)
                board[r][c] = 0
        col = 0 

    return max_knights[0]

# Hàm chính
def solve_knights(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    max_knights_result = [0]  # Dùng mảng để lưu giá trị tham chiếu
    knights(board, n, 0, max_knights_result, 0, 0)
    print(f"Số quân mã tối đa có thể đặt trên bàn cờ {n}x{n}: {max_knights_result[0]}")

solve_knights(4)

