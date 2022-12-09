class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        used = set()
        n = len(s)

        def substring(i, count):
            nonlocal used
            ans = count

            if i >= n + 1:
                return 0
            
            for j in range(i+1, n+1):
                if s[i:j] not in used:
                    used.add(s[i:j])
                    ans = max(ans, substring(j, count + 1))
                    used.remove(s[i:j])
            return ans
        
        return substring(0, 0)

