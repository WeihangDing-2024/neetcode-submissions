class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for i in range(9):
            num_set = set()
            for j in range(9):
                if board[i][j] != ".":
                    # print(f"now checking {i}, {j}")
                    if board[i][j] in num_set:
                        return False
                    num_set.add(board[i][j])
        
        # check columns
        for j in range(9):
            num_set = set()
            for i in range(9):
                if board[i][j] != ".":
                    # print(f"now checking {i}, {j}")
                    if board[i][j] in num_set:
                        return False
                    num_set.add(board[i][j])
        
        # check same cube
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                num_set = set()
                for row_idx in range(3):
                    for col_idx in range(3):
                        if board[i+row_idx][j+col_idx] != ".":
                            # print(f"now checking {i+row_idx}, {j+col_idx}")
                            if board[i+row_idx][j+col_idx] in num_set:
                                return False
                            num_set.add(board[i+row_idx][j+col_idx])
        return True
        