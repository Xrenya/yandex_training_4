ROWS, COLS = map(int, input().strip().split())

mat = []
max_side = 0
dp = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
for row in range(1, ROWS + 1):
    mat = list(map(int, input().strip().split()))
    for col in range(1, COLS + 1):
        if mat[col - 1]:
            dp[row][col] += min(dp[row - 1][col], dp[row - 1][col - 1], dp[row][col - 1]) + 1
            max_side = max(max_side, dp[row][col])

print(max_side)
