class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        n = 9
        def checkRow():
            for i in range(n):
                nums = set()
                for j in range(n):
                    if board[i][j] != "." and board[i][j] in nums:
                        # print(f"detected in row, {i}, {j}")
                        return False
                    nums.add(board[i][j])
            return True
        
        def checkCol():
            for i in range(n):
                nums = set()
                for j in range(n):
                    if board[j][i] != "." and board[j][i] in nums:
                        # print(f"detected in col, {j}, {i}")
                        return False
                    nums.add(board[j][i])
            return True
        
        def checkGrid():
            start = [0, 3, 6]
            for i in start:
                for j in start:
                    nums = set()
                    for row in range(i, i+3):
                        for col in range(j, j+3):
                            if board[row][col] != "." and board[row][col] in nums:
                                # print(f"detected in gird, {i}, {j}")
                                return False
                            nums.add(board[row][col])
            return True
        
        return checkRow() and checkCol() and checkGrid()
        