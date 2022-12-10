class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
           for j in range(9):
               if board[i][j] != '.':
                   num = int(board[i][j])
                   row[i].add(num)
                   col[j].add(num)

                   box_id = i // 3 * 3 + j // 3
                   boxes[box_id].add(num)
                   
        def sudoku(i, j):
            nonlocal solved
            new_i = i + (j+1) // 9
            new_j = (j+1) % 9

            if i == 9:
                solved = True
                return

            if board[i][j] != '.':
                sudoku(new_i, new_j)
            else:
                for num in range(1, 10):
                    box_id = i // 3 * 3 + j // 3
                    if num not in row[i] and num not in col[j] and num not in boxes[box_id]:
                        row[i].add(num)
                        col[j].add(num)
                        boxes[box_id].add(num)

                        board[i][j] = str(num)
                        sudoku(new_i, new_j)
                        
                        if not solved:
                            row[i].remove(num)
                            col[j].remove(num)
                            boxes[box_id].remove(num)
                            board[i][j] = '.'
        
        solved = False
        sudoku(0, 0)
        
