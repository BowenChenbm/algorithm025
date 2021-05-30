#51. N 皇后
# 位运算解法：
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def gen_board():
            board = list()
            for i in range(n):
                row[queens[i]] = "Q"
                board.append("".join(row))
                row[queens[i]] = "."
            return board

        def DFS(row: int, columns: int, pie: int, na: int):
            if row == n:
                board = gen_board()
                result.append(board)
            else:
                bits = (~(columns | pie | na)) & ((1 << n)- 1) #当前空位
                while bits:
                    p = bits & -bits #取最低位1
                    bits = bits & (bits - 1) #在P位置放入皇后
                    column = bin(p - 1).count("1")
                    queens[row] = column
                    DFS(row + 1, columns | p, (pie | p) << 1, (na | p) >> 1)

        result = list()
        queens = [-1] * n
        row = ["."] * n
        DFS(0, 0, 0, 0)
        return result
