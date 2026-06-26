class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(row, col, word_idx, visited):
            # print(f"curr {row}, {col}, idx {word_idx}, visited {visited}")

            if word_idx >= len(word):
                # print('return True')
                return True

            
            if (row, col) in visited:
                # print('return False')
                return False

            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                # print('return False')
                return False

            if board[row][col] == word[word_idx]:
                visited.add((row, col))
                if (dfs(row+1, col, word_idx+1, visited) or
                    dfs(row-1, col, word_idx+1, visited) or
                    dfs(row, col+1, word_idx+1, visited) or
                    dfs(row, col-1, word_idx+1, visited)):
                    return True
                visited.remove((row, col))
            # print('return False')
            return False

        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if dfs(i, j, 0, set()):
                    return True
        return False
        