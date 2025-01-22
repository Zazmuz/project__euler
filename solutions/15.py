dp = {}
def dfs(pos):
    if pos in dp:
        return dp[pos]
    size = 20
    x, y = pos
    if x == size and y == size:
        return 1

    s = 0
    if x < size:
        s += dfs((x+1,y))
    if y < size:
        s += dfs((x,y+1))

    dp[pos] = s
    return s

print(dfs((0,0)))