class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        if m == 0:
            return n
        if n == 0:
            return m

        dp = [[-1] * (n+1) for _ in range(m+1)]

        for j in range(n+1):
            dp[m][j] = n - j 
        for i in range(m+1):
            dp[i][n] = m - i
        
        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                if word1[row] == word2[col]:
                    dp[row][col] = dp[row+1][col+1]
                else:
                    dp[row][col] = min(dp[row+1][col], dp[row][col+1], dp[row+1][col+1]) + 1
        
        return dp[0][0]
