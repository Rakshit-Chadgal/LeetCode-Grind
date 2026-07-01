class Solution:
    def findDegrees(self, matrix):
        n = len(matrix)
        ans = [0] * n

        for i in range(n):
            degree = 0
            for j in range(n):
                if matrix[i][j] == 1:
                    degree += 1
            ans[i] = degree

        return ans