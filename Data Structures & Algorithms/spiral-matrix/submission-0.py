class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        top, right, down, left = 0, n-1, m-1, 0
        res = []

        while top < down and left < right:
            # go right
            for i in range(left, right+1):
                res.append(matrix[top][i])
            top += 1

            # go down
            for i in range(top, down+1):
                res.append(matrix[i][right])
            right -= 1

            # go left
            for i in range(right, left-1, -1):
                res.append(matrix[down][i])
            down -= 1

            # go up
            for i in range(down, top-1, -1):
                res.append(matrix[i][left])
            left += 1
        
        if left == right:
            for i in range(top, down+1):
                res.append(matrix[i][left])
        elif top == down and left != right:
            for i in range(left, right+1):
                res.append(matrix[top][i])

        return res