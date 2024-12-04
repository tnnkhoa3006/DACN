# Reimporting necessary libraries and recreating the visualization due to the state reset.
import matplotlib.pyplot as plt

# Dữ liệu
board_sizes = [4, 5, 6, 7, 8, 9, 10]
backtracking_results = [8, 13, 18, 25, None, None, None]
greedy_results = [8, 13, 18, 23, 32, 40, 50]
hill_climbing_results = [8, 13, 18, 25, 32, 41, 47]

# Vẽ biểu đồ
plt.figure(figsize=(10, 6))

# Backtracking với chú thích lỗi
plt.plot(board_sizes, backtracking_results, marker='o', label='Backtracking (error beyond 7)', linestyle='dashed', color='red', linewidth=2)
plt.scatter([8, 9, 10], [None, None, None], label='Backtracking Error', color='red', marker='x', s=100)

# Greedy
plt.plot(board_sizes, greedy_results, marker='s', label='Greedy', linestyle='solid', color='blue', linewidth=2)

# Hill Climbing
plt.plot(board_sizes, hill_climbing_results, marker='^', label='Hill Climbing', linestyle='dotted', color='green', linewidth=2)

# Tô sáng vùng mà Backtracking không hoạt động
plt.axvspan(8, 10, color='grey', alpha=0.2, label='Backtracking Limit')

# Điều chỉnh khoảng cách giữa các đường để tránh đè lên nhau
for i, size in enumerate(board_sizes):
    if i < 4:  # Các giá trị trùng nhau ở kích thước nhỏ
        plt.text(size, greedy_results[i] + 0.5, f'{greedy_results[i]}', color='blue', fontsize=10)
        plt.text(size, hill_climbing_results[i] - 0.5, f'{hill_climbing_results[i]}', color='green', fontsize=10)
    elif i >= 4:  # Giá trị lớn hơn rõ ràng hơn
        plt.text(size - 0.2, greedy_results[i] + 1, f'{greedy_results[i]}', color='blue', fontsize=10)
        plt.text(size + 0.2, hill_climbing_results[i] - 1, f'{hill_climbing_results[i]}', color='green', fontsize=10)

# Tùy chỉnh biểu đồ
plt.title("So sánh hiệu suất thuật toán qua số lượng quân mã tối ưu", fontsize=14)
plt.xlabel("Kích thước bàn cờ (n x n)", fontsize=12)
plt.ylabel("Số lượng quân mã tối ưu", fontsize=12)
plt.xticks(board_sizes)
plt.grid(alpha=0.3)
plt.legend(fontsize=12, loc='upper left')
plt.tight_layout()

# Hiển thị
plt.show()
