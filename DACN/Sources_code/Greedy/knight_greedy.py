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
    max_knights = (n * n) // 2  # Số quân mã tối đa
    placed_knights = 0  # Số quân mã đã đặt

    for row in range(n):
        for col in range(n):
            if (row + col) % 2 == 0:  # Tham lam đặt trên ô trắng trước (ô đen cũng hợp lệ)
                if is_valid_move(board, row, col, n):
                    board[row][col] = 1  # Đặt quân mã
                    placed_knights += 1
                    if placed_knights == max_knights:
                        return board

    return board


def print_board(board):
    """In bàn cờ dưới dạng ma trận."""
    for row in board:
        print(" ".join("K" if cell == 1 else "." for cell in row))


# Sử dụng
n = 11  # Kích thước bàn cờ
board = greedy_knight_placement(n)
print(f"Bàn cờ {n}x{n} với tối đa {len(board) * len(board[0]) // 2} quân mã:")
print_board(board)
