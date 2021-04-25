# 200, 岛屿数量
# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。此外，你可以假设该网格的四条边均被水包围。

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        lenght_row = len(grid)
        if lenght_row == 0: return 0
        lenght_column = len(grid[0])
        iland_result = 0
        def dfs(grid, r, c):
            grid[r][c] = 0
            for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= x < lenght_row and 0 <= y < lenght_column and grid[x][y] == "1":
                    dfs(grid, x, y)

        for r in range(lenght_row):
            for c in range(lenght_column):
                if grid[r][c] == "1":
                    iland_result += 1
                    dfs(grid, r, c)

        return iland_result
