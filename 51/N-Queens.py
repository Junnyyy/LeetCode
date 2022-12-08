class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        pDiag = set() 
        nDiag = set()

        result = []
        board = [["."] * n for _ in range(n)]

        def nQueens(r):
            if r == n:
                rowCopy = ["".join(row) for row in board]
                result.append(rowCopy)
                return

            for c in range(n):
                if c in col or (r + c) in pDiag or (r - c) in nDiag:
                    continue

                col.add(c)
                pDiag.add(r+c)
                nDiag.add(r-c)
                board[r][c] = "Q"

                nQueens(r+1)

                col.remove(c)
                pDiag.remove(r+c)
                nDiag.remove(r-c)
                board[r][c] = "."

        nQueens(0)
        return result

