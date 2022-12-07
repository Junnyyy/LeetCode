class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        cache = [[False] * (len(s2) + 1) for _ in range(len(s1)+1)]
        cache[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i+j] and cache[i + 1][j]:
                    cache[i][j] = True
                if j < len(s2) and s2[j] == s3[i+j] and cache[i][j+1]:
                    cache[i][j] = True
        
        return cache[0][0]

