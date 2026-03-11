# src/eight_queens.py
def solve_n_queens(n: int) -> list[list[str]]:
    """
    求解N皇后问题，返回所有合法棋盘布局
    :param n: 皇后数量/棋盘大小
    :return: 所有解的列表，每个解是n行字符串组成的棋盘
    """
    solutions = []
    cols = set()       # 已占用的列
    pie = set()        # 正对角线（row + col 固定）
    na = set()         # 反对角线（row - col 固定）

    def backtrack(row: int, path: list[int]) -> None:
        if row == n:
            # 生成可视化棋盘
            board = []
            for col in path:
                line = ['.'] * n
                line[col] = 'Q'
                board.append(''.join(line))
            solutions.append(board)
            return
        
        for col in range(n):
            # 🔥 这里故意留个位置：等下引入Bug时改这里！
            if col in cols or (row + col) in pie or (row + col) in na:
                continue
            # 放置皇后
            cols.add(col)
            pie.add(row + col)
            na.add(row - col)
            path.append(col)
            # 递归下一行
            backtrack(row + 1, path)
            # 回溯撤销
            path.pop()
            na.remove(row - col)
            pie.remove(row + col)
            cols.remove(col)

    backtrack(0, [])
    return solutions

# 测试运行（可选）
if __name__ == "__main__":
    n = 8
    res = solve_n_queens(n)
    print(f"8皇后问题共有 {len(res)} 个解")
    for line in res[0]:
        print(line)